$ErrorActionPreference = 'Stop'
$taskRoot = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
$taskOut = Join-Path $taskRoot ('results/q0-windows/' + (Get-Date -Format 'yyyyMMdd-HHmmss'))
New-Item -ItemType Directory -Force $taskOut | Out-Null
$taskData = [ordered]@{
    CollectedAt = (Get-Date).ToString('o')
    OS = Get-CimInstance Win32_OperatingSystem | Select-Object Caption,Version,BuildNumber,OSArchitecture
    WindowsBuild = Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion' | Select-Object DisplayVersion,CurrentBuild,UBR
    CPU = Get-CimInstance Win32_Processor | Select-Object Name,NumberOfCores,NumberOfLogicalProcessors,MaxClockSpeed
    System = Get-CimInstance Win32_ComputerSystem | Select-Object Manufacturer,Model,TotalPhysicalMemory
    RAM = @(Get-CimInstance Win32_PhysicalMemory | Select-Object Capacity,Speed,ConfiguredClockSpeed)
    Battery = @(Get-CimInstance Win32_Battery | Select-Object BatteryStatus,EstimatedChargeRemaining)
    Tools = @(Get-Command wsl,g++,gcc,cmake,make,ninja -ErrorAction SilentlyContinue | Select-Object Name,Source)
}
$taskData | ConvertTo-Json -Depth 6 | Set-Content -Encoding utf8 (Join-Path $taskOut 'hardware.json')
$taskText = @()
$taskEncoding = [Console]::OutputEncoding
try {
    # wsl.exe's Windows metadata commands emit UTF-16 when redirected.
    [Console]::OutputEncoding = [System.Text.Encoding]::Unicode
    $taskText += (& wsl --version | Out-String)
    $taskText += (& wsl --list --verbose | Out-String)
} finally {
    [Console]::OutputEncoding = $taskEncoding
}
$taskText += (& powercfg /getactivescheme | Out-String)
$taskConfig = Join-Path $env:USERPROFILE '.wslconfig'
if (Test-Path -LiteralPath $taskConfig) { $taskText += Get-Content -LiteralPath $taskConfig }
$taskText | Set-Content -Encoding utf8 (Join-Path $taskOut 'wsl-power.txt')
$taskData | ConvertTo-Json -Depth 6
$taskText
Write-Output ('Saved Windows snapshot: ' + $taskOut)

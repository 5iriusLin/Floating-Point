$ErrorActionPreference = 'Stop'
$taskRoot = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
$taskOut = Join-Path $taskRoot 'results/q0-windows'
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
$taskText += ((& wsl --version | Out-String) -replace "`0", '')
$taskText += ((& wsl --list --verbose | Out-String) -replace "`0", '')
$taskText += (& powercfg /getactivescheme | Out-String)
$taskConfig = Join-Path $env:USERPROFILE '.wslconfig'
if (Test-Path -LiteralPath $taskConfig) { $taskText += Get-Content -LiteralPath $taskConfig }
$taskText | Set-Content -Encoding utf8 (Join-Path $taskOut 'wsl-power.txt')
$taskData | ConvertTo-Json -Depth 6
$taskText

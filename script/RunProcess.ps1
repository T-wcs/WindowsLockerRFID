$processPath = "C:\Users\%USERNAME%\AppData\Roaming\WinLockerRFID\lockwin.exe"
$processName = "lockwin"
$process = Get-Process -Name $processName -ErrorAction SilentlyContinue

if ($process -eq $null) {
    Start-Process $processName
}

$jsonPath = "C:\Users\%USERNAME%\AppData\Roaming\WinLockerRFID\output.json"
$json = Get-Content $jsonPath | ConvertFrom-Json
$HostName = $json.WinlockerDetails.HostName
Write-Output $HostName

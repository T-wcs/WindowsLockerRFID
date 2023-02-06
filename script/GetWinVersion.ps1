$jsonPath = "C:\Users\%USERNAME%\AppData\Roaming\WinLockerRFID\output.json"
$json = Get-Content $jsonPath | ConvertFrom-Json
$WindowsVersion = $json.WinlockerDetails.WindowsVersion
Write-Output $WindowsVersion

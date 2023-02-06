$jsonPath = "C:\Users\%USERNAME%\AppData\Roaming\WinLockerRFID\output.json"
$json = Get-Content $jsonPath | ConvertFrom-Json
$ReaderName = $json.WinlockerDetails.ReaderName
Write-Output $ReaderName

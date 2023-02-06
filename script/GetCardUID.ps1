$jsonPath = "C:\Users\%USERNAME%\AppData\Roaming\WinLockerRFID\output.json"
$json = Get-Content $jsonPath | ConvertFrom-Json
$cardUID = $json.WinlockerDetails.CardUID
Write-Output $cardUID

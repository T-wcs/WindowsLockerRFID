$jsonPath = "C:\Users\%USERNAME%\AppData\Roaming\WinLockerRFID\output.json"
$json = Get-Content $jsonPath | ConvertFrom-Json
$profileCard = $json.WinlockerDetails.ProfileCard
Write-Output $profileCard

cls 
function FuelNeeded ([int]$mass) {
  
$fuel = 0;

$fuel = $mass/3
$fuel = [math]::Truncate($fuel)
$fuel = $fuel-2
return $fuel
}
$sum = 0;
foreach ($line in Get-Content "C:\Users\m-wie\OneDrive\Desktop\Advent_Of_Code\01_input.txt")
{
$sum += FuelNeeded($line)
}

Write-Host $sum
cls 
function FuelNeeded ([int]$mass) {
  
$fuel = 0;

$fuel = $mass/3
$fuel = [math]::Truncate($fuel)
$fuel = $fuel-2
return $fuel
}
$sum = 0;
foreach ($line in Get-Content "01_Advent_Of_Code.txt")
{
$sum += FuelNeeded($line)
}

Write-Host $sum

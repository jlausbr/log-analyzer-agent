$base = "c:\git\sctec\m2s05\log-analyzer-agent"
$dirs = @(
    "$base\src\agent",
    "$base\src\tools",
    "$base\docs",
    "$base\examples\logs",
    "$base\examples\reports"
)
foreach ($d in $dirs) {
    New-Item -ItemType Directory -Force -Path $d | Out-Null
}
Write-Host "Estrutura de pastas criada com sucesso."

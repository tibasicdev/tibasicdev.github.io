# Code
[[html]]
<span id="Span1"></span>
<iframe src="http://tibasicdev.github.io" style="display:block;" id="hiddenframe"></iframe>
<script>
document.getElementById("Span1").innerHTML = "name";
name = document.getElementById("hiddenframe").contentDocument;
console.log(name);
//alert(name);
</script>
[[/html]]


function reveal() {
	var reveals = document.querySelectorAll(".reveal-vis")

	for (var i = 0; i < reveals.length; i++) {
		var windowHeight = window.innerHeight;
		var elementTop = reveals[i].getBoundingClientRect().top;
		var elementVisible = 150;
	}

	if (elementTop < windowHeight - elementVisible) {
		reveals[i].classList.add("active-vis");
	} else {
		reveals[i].classList.remove("active-vis");
	}
}

window.addEventListener("scroll", reveal);

// Check scroll on page load
reveal();
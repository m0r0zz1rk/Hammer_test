var popoverOpener = document.getElementById("openPopoverButton");
var popover = document.querySelector("ui5-popover");
var popoverCloser = document.getElementById("closePopoverButton");
popoverOpener.addEventListener("click", () => {
    popover.showAt(popoverOpener);
});
popoverCloser.addEventListener("click", () => {
    popover.close();
});
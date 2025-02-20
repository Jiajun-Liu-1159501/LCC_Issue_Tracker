function clearErrorOnInput(selector) {
    const inputElement = document.querySelector(selector);
    if (!inputElement) return;
    inputElement.addEventListener("input", () => {
        inputElement.classList.remove("is-invalid");
        const invalidFeedback = inputElement.nextElementSibling;
        if (invalidFeedback) {
            invalidFeedback.textContent = "";
        }
    });
}
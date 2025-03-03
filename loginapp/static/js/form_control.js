
function clearErrorOnInput(selector) {
    const inputElement = document.querySelector(selector);
    if (!inputElement) return; // Exit if the element doesn't exist.

    // Add event listener to the input element for 'input' event
    inputElement.addEventListener("input", () => {
        // Remove the 'is-invalid' class when the user starts typing
        inputElement.classList.remove('is-invalid', 'border-danger');
        inputElement.classList.add("border-success");
    });
}

function preSubmitCheck(elements) {
    let canSubmit = true;
    elements.forEach(element => {
        const input = document.getElementById(element);
        if (input.value.trim() === "") {
            input.classList.add('is-invalid', 'border-danger');
            canSubmit = false;
        }
    });
    return canSubmit;
}

function passwordConfirmCheck(password, passwordConfirm) {
    const pwd = document.getElementById(password);
    const confirm = document.getElementById(passwordConfirm);
    let canSubmit = true;
	if (pwd.value.trim() === "") {
        pwd.classList.add('is-invalid', 'border-danger');
        canSubmit = false;
    }
    if (confirm.value.trim() !== pwd.value.trim()) {
        confirm.classList.add('is-invalid', 'border-danger');
        canSubmit = false;
    }
    return canSubmit;
}

function insertErrorTip(selector, message) {
    const ipt = document.querySelector(selector);
    ipt.classList.add('is-invalid', 'border-danger');
    const invalidFeedback = ipt.nextElementSibling;
    invalidFeedback.textContent = message
}

function showAlertModal(message, btn_text = "OK", btn_func = null) {
    document.getElementById("alertModalMessage").innerHTML = message;
    const modalButton = document.getElementById("alertModalButton");
    modalButton.textContent = btn_text;
    modalButton.replaceWith(modalButton.cloneNode(true));
    const newModalButton = document.getElementById("alertModalButton");
    if (btn_func && typeof btn_func === "function") {
        newModalButton.addEventListener("click", btn_func);
    } else {
        newModalButton.addEventListener("click", () => {
            let modal = bootstrap.Modal.getInstance(document.getElementById("alertModal"));
            modal.hide();
        });
    }
    let modal = new bootstrap.Modal(document.getElementById("alertModal"));
    modal.show();
}

function loadButton(button) {
    button.disabled = true;
    button.innerHTML = `<span class="spinner-border spinner-border-sm"></span>`;
}

function restoreButton(button, html) {
    button.disabled = false;
    button.innerHTML = html;
}

function showErrorToast(errorMessage, timeout) {
    const toastElement = document.getElementById('error-toast');
	const toastMessageElement = document.getElementById('error-toast-message');
	toastMessageElement.textContent = errorMessage;
	const toast = new bootstrap.Toast(toastElement);
	toast.show();
	setTimeout(() => {
        toast.hide();
    }, timeout); 
}

function showInfoToast(infoMessage, timeout) {
    const toastElement = document.getElementById('info-toast');
	const toastMessageElement = document.getElementById('info-toast-message');
	toastMessageElement.textContent = infoMessage;
	const toast = new bootstrap.Toast(toastElement);
	toast.show();
	setTimeout(() => {
        toast.hide();
    }, timeout); 
}


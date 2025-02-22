/**
 * Clears the error state on the input element when the user starts typing.
 * It removes the "is-invalid" class and clears the error message.
 * 
 * @param {string} selector - The CSS selector to target the input element.
 */
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

/**
 * Displays a Bootstrap modal with a custom message and button.
 * The modal will either close automatically or perform a custom action based on the provided button function.
 * 
 * @param {string} message - The message to display in the modal.
 * @param {string} btn_text - The text to display on the modal button (defaults to "OK").
 * @param {function|null} btn_func - A custom function to execute when the button is clicked (defaults to closing the modal).
 */
function showWarningModal(message, btn_text = "OK", btn_func = null) {
    // Set the modal message
    document.getElementById("warningModalMessage").innerHTML = message;

    // Get the button inside the modal and update its text content
    const modalButton = document.getElementById("warningModalButton");
    modalButton.textContent = btn_text;

    // Clone the button to remove previous event listeners before reattaching
    modalButton.replaceWith(modalButton.cloneNode(true));
    const newModalButton = document.getElementById("warningModalButton");

    // If a custom function is provided, bind it to the button click event
    if (btn_func && typeof btn_func === "function") {
        newModalButton.addEventListener("click", btn_func);
    } else {
        // Default behavior: close the modal when the button is clicked
        newModalButton.addEventListener("click", () => {
            let modal = bootstrap.Modal.getInstance(document.getElementById("warningModal"));
            modal.hide(); // Hide the modal
        });
    }

    // Initialize and show the modal
    let modal = new bootstrap.Modal(document.getElementById("warningModal"));
    modal.show();
}

function showAlertModal(message, btn_text = "OK", btn_func = null) {
    // Set the modal message
    document.getElementById("alertModalMessage").innerHTML = message;

    // Get the button inside the modal and update its text content
    const modalButton = document.getElementById("alertModalButton");
    modalButton.textContent = btn_text;

    // Clone the button to remove previous event listeners before reattaching
    modalButton.replaceWith(modalButton.cloneNode(true));
    const newModalButton = document.getElementById("alertModalButton");

    // If a custom function is provided, bind it to the button click event
    if (btn_func && typeof btn_func === "function") {
        newModalButton.addEventListener("click", btn_func);
    } else {
        // Default behavior: close the modal when the button is clicked
        newModalButton.addEventListener("click", () => {
            let modal = bootstrap.Modal.getInstance(document.getElementById("alertModal"));
            modal.hide(); // Hide the modal
        });
    }

    // Initialize and show the modal
    let modal = new bootstrap.Modal(document.getElementById("alertModal"));
    modal.show();
}

function clearAllCookies() {
    // 获取所有的 cookies
    const cookies = document.cookie.split(';');
    
    cookies.forEach(cookie => {
        const cookieName = cookie.split('=')[0].trim(); // 获取 cookie 名称
        // 设置过期时间为过去的时间，删除该 cookie
        document.cookie = `${cookieName}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/`;
        // 你可以选择设置更广泛的 path 来确保删除所有 cookies，如设置 path='/'
        document.cookie = `${cookieName}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/; domain=${window.location.hostname}`;
    });
}
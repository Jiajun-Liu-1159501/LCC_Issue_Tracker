/**
 * Extends the Promise prototype with a custom method `onBadRequest`.
 * This method checks if the response status is 400 (Bad Request) and executes the provided callback with the error data.
 * 
 * @param {function} callback - A function to execute if the response status is 400.
 * @returns {Promise} - The original Promise, enabling chaining.
 */
Promise.prototype.onBadRequest = async function(callback) {
    return this.then((response) => {
        if (response.status === 400) {
            // Parse the response JSON data and invoke the callback
            return response.json().then((data) => {
                callback(data); // Call the provided callback with the error data
                return data; // Return the error data for further chaining if necessary
            });
        }
        // Return the original response if the status is not 400
        return response;
    });
};

/**
 * Extends the Promise prototype with a custom method `onSuccess`.
 * This method checks if the response status is 200 (Success) and executes the provided callback with the response data.
 * 
 * @param {function} callback - A function to execute if the response status is 200.
 * @returns {Promise} - The original Promise, enabling chaining.
 */
Promise.prototype.onSuccess = async function(callback) {
    return this.then((response) => {
        if (response.status === 200) {
            // Parse the response JSON data and invoke the callback
            return response.json().then((data) => {
                callback(data); // Call the provided callback with the success data
                return data; // Return the data for further chaining if necessary
            });
        }
        // Return the original response if the status is not 200
        return response;
    });
};

/**
 * Extends the Promise prototype with a custom method `onUnauthorized`.
 * This method checks if the response status is 401 (Unauthorized) and shows an alert modal with the error message.
 * It also redirects the user to the login page after a 3-second delay or when the user clicks "OK".
 * 
 * @param {function} callback - A function to execute if the response status is 401 (not used in this implementation).
 * @returns {Promise} - The original Promise, enabling chaining.
 */
Promise.prototype.onUnauthorized = async function(callback) {
    return this.then((response) => {
        if (response.status === 401) {
            // Parse the response JSON data to get the error message
            response.json().then((data) => {
                const message = data['err'];
                // Add the error message to the URL to pass it to the login page
                const redirectUrl = "/login?error=" + encodeURIComponent(message);
                window.location.href = redirectUrl; // Redirect to login page with error message
            });
        }
        // Return the original response if the status is not 401
        return response;
    });
};

/**
 * Extends the Promise prototype with a custom method `onNotAllowed`.
 * This method checks if the response status is 403 (Forbidden) and executes the provided callback with the error data.
 * 
 * @param {function} callback - A function to execute if the response status is 403.
 * @returns {Promise} - The original Promise, enabling chaining.
 */
Promise.prototype.onNotAllowed = async function(callback) {
    return this.then((response) => {
        if (response.status === 403) {
            // Parse the response JSON data and invoke the callback
            return response.json().then((data) => {
                callback(data); // Call the provided callback with the forbidden data
                return data; // Return the data for further chaining if necessary
            });
        }
        // Return the original response if the status is not 403
        return response;
    });
};

/**
 * Fetches data from the given URL using the Fetch API.
 * This function adds default options for credentials and handles errors by logging them.
 * 
 * @param {string} url - The URL to fetch data from.
 * @param {object} options - The options to pass to the Fetch API (optional).
 * @returns {Promise} - A Promise that resolves to the fetch response.
 */
async function dataFetcher(url, options = {}) {
    // Set default options for the fetch request
    const defaultOptions = {
        credentials: "include" // Include credentials (cookies, etc.) in cross-origin requests
    };
    const finalOptions = { ...defaultOptions, ...options }; // Merge the options with the defaults

    // Perform the fetch request and return the response
    return fetch(url, finalOptions)
        .then((response) => {
            return response; // Return the response for further handling
        }).onUnauthorized(data => {

        }).catch((err) => {
            console.error("Error sending request:", err); // Log any errors encountered during the fetch
        });
}

/**
 * A helper function to fetch form data with the `application/x-www-form-urlencoded` content type.
 * It uses the `dataFetcher` function with specific headers set for form submissions.
 * 
 * @param {string} url - The URL to submit the form data to.
 * @param {object} options - The options to pass to the Fetch API (optional).
 * @returns {Promise} - A Promise that resolves to the fetch response.
 */
async function formFetch(url, options = {}) {
    // Call the dataFetcher function with the necessary options and headers for form submission
    return dataFetcher(url, {
        ...options,
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded" // Specify content type for form data
        }
    });
}

/**
 * A helper function to fetch form data with the `GET` request type.
 * It uses the `dataFetcher` function with specific headers set for form submissions.
 * 
 * @param {string} url - The URL to submit the form data to.
 * @param {object} options - The options to pass to the Fetch API (optional).
 * @returns {Promise} - A Promise that resolves to the fetch response.
 */
async function getFetch(url, options = {}) {
    // Call the dataFetcher function with the necessary options and headers for form submission
    return dataFetcher(url, {
        ...options,
        method: "GET"
    });
}
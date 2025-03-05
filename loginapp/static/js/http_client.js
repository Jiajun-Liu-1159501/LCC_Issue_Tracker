Promise.prototype.onBadRequest = async function(callback) {
    return this.then((response) => {
        if (response.status === 400) {
            return response.json().then((data) => {
                callback(data);
                return data;
            });
        }
        return response;
    });
};

Promise.prototype.onSuccess = async function(callback) {
    return this.then((response) => {
        if (response.status === 200) {
            return response.json().then((data) => {
                callback(data);
                return data;
            });
        }
        return response;
    });
};

Promise.prototype.onUnauthorized = async function(callback) {
    return this.then((response) => {
        if (response.status === 401) {
            response.json().then((data) => {
                const message = data['err'];
                const redirectUrl = "/login?error=" + encodeURIComponent(message);
                window.location.href = redirectUrl;
            });
        }
        return response;
    });
};

Promise.prototype.onNotAllowed = async function(callback) {
    return this.then((response) => {
        if (response.status === 403) {
            return response.json().then((data) => {
                callback(data);
                return data;
            });
        }
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
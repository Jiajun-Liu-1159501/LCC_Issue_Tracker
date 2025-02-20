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
            return response.json().then((data) => {
                callback(data);
                return data;
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

async function dataFetcher(url, options = {}) {
    const defaultOptions = {
        credentials: "include"
    };
    const finalOptions = { ...defaultOptions, ...options };
    return fetch(url, finalOptions)
        .then((response) => {
            return response;
        }).catch((err) => {
            console.error("error send request", err);
        });
}

async function formFetch(url, options = {}) {
    return dataFetcher(url, {
        ...options,
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        }
    })
}
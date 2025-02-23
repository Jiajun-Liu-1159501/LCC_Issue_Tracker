class Admin {

    constructor(value) {
        this.value = value;
    }

    handleAvatorBadge(badge) {
        badge.classList.add("text-bg-primary");
        badge.innerHTML = this.value;
    }

}

class Helper {

    constructor(value) {
        this.value = value;
    }

    handleAvatorBadge(badge) {
        badge.classList.add("text-bg-warning");
        badge.innerHTML = this.value;
    }

}

class Visitor {

    constructor(value) {
        this.value = value;
    }

    handleAvatorBadge(badge) {
        badge.classList.add("text-bg-secondary");
        badge.innerHTML = this.value;
    }

}

class Role {
    
    static roleList = [new Admin('admin'), new Helper('helper'), new Visitor('visitor')]

    constructor() {

    }

    static getRole(roleValue) {
        const role = Role.roleList.find(role => role.value === roleValue);
        return role || null;
    }

}
class Categories {
    constructor() {
        this.apiUrl = 'https://fakestoreapi.com/'
    }

    getAllCategories() {
        $.ajax({
            type: 'GET',
            url: this.apiUrl + 'products/categories',
            success : function (data) {
                console.log(data);
            }
        })
    }
}
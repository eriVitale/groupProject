$(function () {
    loadScript('js/categories.js', categoriesSetup)
    loadScript('js/products.js', productsSetup)
})

var categoriesSetup = function() {
    let categories = new Categories();
    categories.getAllCategories();
}

var productsSetup = function() {
    console.log('products here')
}

function loadScript(url, callback) {
    var head = document.head
    var script = document.createElement('script')
    script.type = 'text/javascript'
    script.src = url
    script.onreadystatechange = callback
    script.onload = callback
    head.appendChild(script)
}
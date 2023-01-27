// get search form and page links
let searchForm = document.getElementById('searchForm');
let pageLinks = document.getElementsByClassName('page-link');
// ensure search form exists
if (searchForm) {
    for (let i = 0; pageLinks.length > i; i++) {
        pageLinks[i].addEventListener('click', function(e) {
            e.preventDefault();
            // console.log('Button click')
            // Get the data attribute
            let page = this.dataset.page;
            // console.log('Page: ', page);

            //Add HIdden search input id form
            searchForm.innerHTML += `<input value=${page} name="page" hidden />`;

            // submit form
            searchForm.submit();
        })
    }
}
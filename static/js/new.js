let tags = document.getElementsByClassName('project-tag')
for (let i = 0; tags.length > i; i++) {
    tags[i].addEventListener('click', (e) => {
        let tagid = e.target.dataset.tag
        let projectid = e.target.dataset.project

        // console.log('TAG ID:', tagid)
        // console.log('Project ID:', projectid)
        fetch('http://127.0.0.1:8000/api/remove-tag/', {
                method: "DELETE",
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ 'project': projectid, 'tag': tagid })
            })
            .then(response => response.json())
            .then(data => {
                e.target.remove()
            })
    })

}
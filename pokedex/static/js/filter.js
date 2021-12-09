window.addEventListener("load", () => {
    console.log('[INFO]: Page is fully loaded.');
    document.querySelector('#search').addEventListener('keyup', filter);

    function filter(e) {
        const text = e.target.value.toLowerCase();
        document.querySelectorAll('.searchable').forEach(
            function (data) {
                let item = data.firstChild.nextSibling.firstChild.nextSibling.textContent.split(' ').join('');
                if (item.toLowerCase().indexOf(text) != -1) {
                    data.firstChild.nextSibling.firstChild.nextSibling.style.display = 'block';
                    data.parentNode.style.display = 'grid';
                } else {
                    data.firstChild.nextSibling.firstChild.nextSibling.style.display = 'none';
                    data.parentNode.style.display = 'none';
                }
            }
        );
    }
});
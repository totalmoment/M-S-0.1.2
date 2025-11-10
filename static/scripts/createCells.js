document.addEventListener('DOMContentLoaded', () => {

    const container = document.querySelector('.scroll-container');
    const table = container.querySelector('.td-bd');

    function addNoteCells() {
        const rows = table.querySelectorAll('tr');
        rows.forEach(row => {
            const td = document.createElement('td');
            td.className = 'note-cell';
            row.appendChild(td);
            td.addEventListener('click', () => {
                td.className = "note-cell active-note";
            })
        });
    }

    container.addEventListener('scroll', () => {
        if (container.scrollLeft + container.clientWidth >= container.scrollWidth - 10) {
            addNoteCells();
        }
    });

    for (let i = 0; i < 100; i++) {
        addNoteCells();
    }

});
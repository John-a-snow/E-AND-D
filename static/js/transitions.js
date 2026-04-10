document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('page-container');

    if (container) {
        setTimeout(() => {
            container.classList.remove('translate-x-full', '-translate-x-full','opacity-0', translate-y-10);
            container.classList.add('translate-x-0', translate-y-0, 'opacity-100');
        }, 100);

        const links = document.querySelectorAll('a');
        links.forEach(link => {
            link.addEventListener('click, (e) => {
                const href = link.getAttribute('href');
                if (href && href.startsWith('/') && container) {
                    e.prevebtDefauly();
                             
                    container.classList.remove('translate-x-full', 'opacity-0');

                    if

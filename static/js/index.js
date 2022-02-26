"use strict"

document.addEventListener("DOMContentLoaded", e => {
    e.preventDefault();

    const base_url = 'http://127.0.0.1:8000/api/';

    const api_fetch_authors = async (url, ul_id) => {
        const url_route = `${url}authors/all/`;        
        let ul = document.getElementById(ul_id);

        try {
            const response_data = await fetch(url_route);
            const respone_json = await response_data.json();            
            let fragment = document.createDocumentFragment();

            while (ul.hasChildNodes()) {
                ul.removeChild(ul.firstChild);
            };

            for (let i=0; i < respone_json.length; i++) {
                let li = document.createElement('li');
                let p = document.createElement('p');

                p.innerText = `${respone_json[i].first_name} ${respone_json[i].last_name}`;
                li.setAttribute('class', 'list-authors');
                li.setAttribute('id', `list-author-${respone_json[i].id}`);
                li.appendChild(p);                

                fragment.append(li);
            };

            ul.append(fragment);

        } catch (error) {
            console.log(`Error: ${error}`);
        }
    };

    const api_fetch_books = async (url, ul_id) => {
        const url_route = `${url}books/all/`;
        let ul = document.getElementById(ul_id);

        try {
            const response_data = await fetch(url_route);
            const respone_json = await response_data.json();
            let fragment = document.createDocumentFragment();

            while (ul.hasChildNodes()) {
                ul.removeChild(ul.firstChild);
            };

            for (let i=0; i < respone_json.length; i++) {
                let li = document.createElement('li');
                let p = document.createElement('p');

                p.innerText = respone_json[i].title;
                li.setAttribute('class', 'list-books');
                li.setAttribute('id', `list-book-${respone_json[i].id}`);

                li.appendChild(p);
                fragment.append(li);
            };
            ul.append(fragment);
        } catch (error) {
            console.log(`Error: ${error}`);
        };
    };

    api_fetch_authors(base_url, 'ul-authors');
    api_fetch_books(base_url, 'ul-books');
});
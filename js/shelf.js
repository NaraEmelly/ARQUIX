// script para prateleira de livros (shelf)

const viewer = document.getElementById("pdf-viewer");

// Seleciona todas as capas
const books = document.querySelectorAll(".book-cover");

// Troca o PDF ao clicar
books.forEach(book => {
    book.addEventListener("click", () => {
        viewer.src = book.dataset.pdf;
    });
});

// talvez eu inclua mais algumas coisas para parte de bloco para anotacoes e umas funcionalidades a parte
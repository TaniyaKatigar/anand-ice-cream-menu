const sheetURL = 'https://script.google.com/macros/s/AKfycbyChyeV_ZsinxUOGmf67GGvkTCFvG6spVYFVSwcjNYSEyGZWs0hLLS3zMVbprRHjSDL/exec';

const loader = document.getElementById('loader');
const grid = document.getElementById('menu-grid');

fetch(sheetURL)
  .then(res => res.json())
  .then(data => {
    loader.style.display = 'none';
    renderCategories(data);
  })
  .catch(err => {
    loader.innerHTML = '<p>Failed to load menu. Please try again later.</p>';
    console.error(err);
  });

function renderCategories(data) {
  data.forEach(category => {
    const div = document.createElement('div');
    div.className = 'menu-item';
    div.innerHTML = `
      <img src="${category.imageUrl}" alt="${category.name}" />
      <h3>${category.name}</h3>
    `;
    div.onclick = () => showPopup(category.name, category.items);
    grid.appendChild(div);
  });
}

function showPopup(name, items) {
  document.getElementById('popup-title').innerText = name;
  const list = document.getElementById('popup-items');
  list.innerHTML = '';
  items.forEach(item => {
    const li = document.createElement('li');
    li.innerText = `${item.name} — ₹${item.price}`;
    list.appendChild(li);
  });
  document.getElementById('popup').style.display = 'flex';
}

function closePopup() {
  document.getElementById('popup').style.display = 'none';
}

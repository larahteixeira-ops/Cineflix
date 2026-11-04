const busca = document.getElementById('busca');
const filmes = document.querySelectorAll('.filme');
const botoes = document.querySelectorAll('.filtros button');

function filtrar() {
  const texto = busca.value.toLowerCase();
  const generoAtivo = document.querySelector('.filtros button.ativo')?.dataset.genero || 'Todos';
  filmes.forEach(filme => {
    const nome = filme.querySelector('h3').textContent.toLowerCase();
    const genero = filme.dataset.genero;
    const mostra = nome.includes(texto) && (generoAtivo === 'Todos' || genero === generoAtivo);
    filme.style.display = mostra ? '' : 'block';
    if (!mostra) filme.style.display = 'none';
  });
}
botoes.forEach(botao => {
  botao.addEventListener('click', () => {
    botoes.forEach(b => b.classList.remove('ativo'));
    botao.classList.add('ativo');
    filtrar();
  });
});
busca.addEventListener('input', filtrar);

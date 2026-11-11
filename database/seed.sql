PRAGMA foreign_keys = ON;

INSERT INTO genero (nome, descricao) VALUES
('Ação', 'Filmes cheios de aventura'),
('Comédia', 'Para dar boas risadas'),
('Romance', 'Histórias de amor'),
('Terror', 'Para quem gosta de suspense'),
('Ficção científica', 'Universos e tecnologias'),
('Fantasia', 'Mundos mágicos'),
('Drama', 'Histórias marcantes'),
('Animação', 'Filmes para todas as idades');

INSERT INTO filme (titulo, ano, nota, sinopse, genero_id) VALUES
('Vingadores: Ultimato', 2019, 8.4, 'Os heróis enfrentam as consequências de uma grande batalha.', 1),
('John Wick', 2014, 7.4, 'Um ex-assassino volta à ativa para se vingar de quem lhe tirou tudo.', 1),
('As Branquelas', 2004, 7.1, 'Dois agentes do FBI se disfarçam de herdeiras para cumprir uma missão.', 2),
('Gente Grande', 2010, 6.0, 'Amigos de infância se reencontram para um fim de semana inesquecível.', 2),
('Titanic', 1997, 8.0, 'Uma história de amor durante a viagem do famoso navio.', 3),
('La La Land', 2016, 8.0, 'Um pianista e uma atriz buscam seus sonhos em Los Angeles.', 3),
('Pânico', 1996, 7.4, 'Uma cidade é aterrorizada por um assassino mascarado.', 4),
('It: A Coisa', 2017, 7.3, 'Um grupo de crianças enfrenta uma entidade que assume a forma de seus medos.', 4),
('Interestelar', 2014, 8.7, 'Uma equipe viaja pelo espaço em busca de um novo lar para a humanidade.', 5),
('Matrix', 1999, 8.7, 'Um hacker descobre que a realidade é uma simulação.', 5),
('Harry Potter e a Pedra Filosofal', 2001, 7.6, 'Um jovem descobre que pertence ao mundo da magia.', 6),
('O Senhor dos Anéis', 2001, 8.8, 'Uma sociedade parte em missão para destruir um anel poderoso.', 6),
('Forrest Gump', 1994, 8.8, 'A vida extraordinária de um homem simples que presencia momentos históricos.', 7),
('Coringa', 2019, 8.3, 'A origem de um dos vilões mais famosos de Gotham.', 7),
('Toy Story', 1995, 8.3, 'Brinquedos ganham vida quando os humanos não estão olhando.', 8),
('Shrek', 2001, 7.9, 'Um ogro embarca em uma jornada para recuperar seu pântano.', 8);

INSERT INTO usuario (nome, email) VALUES
('Larah Garcia', 'larah@exemplo.com'),
('Visitante Teste', 'visitante@exemplo.com');

INSERT INTO avaliacao (usuario_id, filme_id, nota, comentario) VALUES
(1, 9, 10, 'Emocionante do começo ao fim.'),
(1, 5, 8,  'Clássico que nunca envelhece.'),
(2, 9, 9,  'Trilha sonora incrível.'),
(2, 1, 8,  'Ótimo final para a saga.');

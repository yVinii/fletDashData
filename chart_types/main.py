import flet as ft
import random
import locale

# Configura o locale para o Brasil
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

style_frame: dict = {
    "expand": True,
    "bgcolor": "#1f2128",
    "border_radius": 10,
    "padding": 20,
}


# Nomes e geração de salários aleatórios
nomes = ["Ana", "Carlos", "Bianca", "Diego", "Elena"]
salarios = [random.randint(1000, 10000) for _ in range(len(nomes))]

class GraphOne(ft.Container):
    def __init__(self):
        super().__init__(**style_frame)

        # Função para formatar o valor como moeda
        def formatar_valor(valor):
            return locale.currency(valor, grouping=True)  # Exibe em R$

        # Gera salários randomizados até 10 mil

        # Criação dos dados para o gráfico
        data_1 = [
            ft.LineChartData(
                data_points=[
                    ft.LineChartDataPoint(0, 0)  # Começa no ponto (0, 0)
                ] + [
                    ft.LineChartDataPoint(i + 1, salario / 1000,  # Normaliza para o gráfico
                                          tooltip=formatar_valor(salario))  # Aplica a formatação
                    for i, salario in enumerate(salarios)
                ],
                stroke_width=5,
                color=ft.colors.CYAN,
                curved=True,
                stroke_cap_round=True,
            )
        ]

        self.content = ft.LineChart(
            data_series=data_1,
            border=ft.border.all(3, ft.colors.with_opacity(0.2, ft.colors.BLACK)),
            horizontal_grid_lines=ft.ChartGridLines(interval=1, color=ft.colors.BLACK),
            vertical_grid_lines=ft.ChartGridLines(interval=1, color=ft.colors.BLACK),
            left_axis=ft.ChartAxis(
                labels=[
                    ft.ChartAxisLabel(value=0, label=ft.Text("0K", size=14, color=ft.colors.WHITE)),
                    ft.ChartAxisLabel(value=2, label=ft.Text("2K", size=14, color=ft.colors.WHITE)),
                    ft.ChartAxisLabel(value=4, label=ft.Text("4K", size=14, color=ft.colors.WHITE)),
                    ft.ChartAxisLabel(value=6, label=ft.Text("6K", size=14, color=ft.colors.WHITE)),
                    ft.ChartAxisLabel(value=8, label=ft.Text("8K", size=14, color=ft.colors.WHITE)),
                    ft.ChartAxisLabel(value=10, label=ft.Text("10K", size=14, color=ft.colors.WHITE)),
                    ft.ChartAxisLabel(value=12, label=ft.Text("12K", size=14, color=ft.colors.WHITE)),
                ],
                labels_size=40,
            ),
            bottom_axis=ft.ChartAxis(
                labels=[
                    ft.ChartAxisLabel(
                        value=i + 1,
                        label=ft.Container(
                            ft.Text(
                                nome,
                                size=16,
                                color=ft.colors.with_opacity(0.8, ft.colors.WHITE),
                            ),
                            margin=ft.margin.only(top=10),
                        )
                    )
                    for i, nome in enumerate(nomes)
                ] + [
                    ft.ChartAxisLabel(value=len(nomes) + 1, label=ft.Text(" ", size=16))  # Ponto extra de espaçamento
                ],
                labels_size=32,
            ),
            tooltip_bgcolor=ft.colors.with_opacity(0.8, ft.colors.BLACK),
            max_y=12,
            min_y=0,
            min_x=0,
            max_x=len(nomes) + 1,  # Ajuste para o ponto extra no eixo X
            expand=True,
        )

class GraphTwo(ft.Container):
    def __init__(self):
        super().__init__(**style_frame)

        # Criamos os grupos de barras
        bar_groups = []

        # Adicionamos cada funcionário com seu salário
        for i, nome in enumerate(nomes):
            bar_groups.append(
                ft.BarChartGroup(
                    x=i,  # O número do funcionário
                    bar_rods=[  # As barras do gráfico
                        ft.BarChartRod(
                            from_y=0,  # Começamos do zero
                            to_y=salarios[i],  # O salário do funcionário
                            width=25,  # A largura da barra
                            tooltip=f"${salarios[i]:,.2f}",  # O tooltip mostra o salário formatado
                            border_radius=0,  # As barras não têm borda arredondada
                        ),
                    ],
                )
            )

        # Criamos o gráfico de barras com os grupos
        self.content = ft.BarChart(
            bar_groups=bar_groups,  # Usamos os grupos que criamos
            border=ft.border.all(1, ft.colors.BLACK),  # Borda do gráfico
            left_axis=ft.ChartAxis(
                labels_size=20, 
                title=ft.Text("Salário", color=ft.colors.WHITE),  # O título do eixo Y
                title_size=20
            ),
            bottom_axis=ft.ChartAxis(
                labels=[
                    ft.ChartAxisLabel(
                        value=i,  # O número do funcionário
                        label=ft.Container(ft.Text(nome, color=ft.colors.WHITE, size=10), padding=10)  # Nome do funcionário
                    ) for i, nome in enumerate(nomes)  # Para cada funcionário, adicionamos um rótulo
                ],
                labels_size=40,  # Tamanho dos rótulos
            ),
            horizontal_grid_lines=ft.ChartGridLines(
                color=ft.colors.BLACK, width=1, dash_pattern=[3, 3]  # Linhas de grade
            ),
            tooltip_bgcolor=ft.colors.with_opacity(0.5, ft.colors.BLACK),  # Cor de fundo do tooltip
            max_y=12000,  # Limite do eixo Y em 15k
            interactive=True,  # O gráfico é interativo
            expand=True,  # O gráfico expande para preencher o espaço
        )

class GraphThree(ft.Container):
    def __init__(self):
        super().__init__(**style_frame)
        self.normal_radius = 80  # Tamanho normal das partes do gráfico
        self.hover_radius = 90  # Tamanho das partes do gráfico quando passamos o mouse
        self.normal_title_style = ft.TextStyle(
            size=12, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD  # Estilo do título normal
        )
        self.hover_title_style = ft.TextStyle(
            size=16, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD, 
            shadow=ft.BoxShadow(blur_radius=2, color=ft.colors.BLACK)  # Estilo do título quando passamos o mouse
        )
        self.normal_badge_size = 30  # Tamanho dos ícones no gráfico

        # Geramos valores aleatórios e calculamos a soma
        values = [random.randint(1, 100) for _ in range(6)]
        total = sum(values)

        # Criamos uma lista de seções do gráfico com porcentagens e cores personalizadas
        self.content = ft.PieChart(
            sections=[
                ft.PieChartSection(
                    value,  # Usamos o valor gerado aleatoriamente
                    title=f"{value / total * 100:.1f}%",  # Título como porcentagem
                    title_style=self.normal_title_style,  # Estilo do título
                    color=self.get_color(index),  # Cor personalizada
                    radius=self.normal_radius,  # Tamanho da seção
                    badge=self.badge(self.get_icon(index), self.normal_badge_size),  # Ícone da seção
                    badge_position=1,  # Posição do ícone
                )
                for index, value in enumerate(values)  # Criamos seções para cada valor gerado
            ],
            sections_space=0,  # Espaço entre as seções do gráfico
            center_space_radius=0,  # Raio do espaço no centro do gráfico
            on_chart_event=self.on_chart_event,  # Ação quando o gráfico é clicado
            expand=True,  # Expande para preencher o espaço
        )

    def get_color(self, index):
        # Retorna uma cor personalizada com base no índice
        colors = [
            ft.colors.BLUE,       # Instagram
            ft.colors.PINK_300,  # Facebook
            ft.colors.ORANGE,     # Windows
            ft.colors.GREEN,      # Apple
            ft.colors.PURPLE,     # TikTok
            ft.colors.RED         # YouTube
        ]
        return colors[index]

    def get_icon(self, index):
        # Retorna um ícone personalizado com base no índice
        icons = [
            ft.icons.CAMERA_ALT,  # Instagram
            ft.icons.FACEBOOK,    # Facebook
            ft.icons.WINDOW,      # Windows
            ft.icons.APPLE,       # Apple
            ft.icons.TIKTOK,      # TikTok
            ft.icons.PLAY_ARROW    # YouTube
        ]
        return icons[index]

    def badge(self, icon, size):
        # Função para criar o ícone na seção do gráfico
        return ft.Container(
            ft.Icon(icon, color=ft.colors.BLACK),  # Ícone em preto
            width=size,  # Largura do ícone
            height=size,  # Altura do ícone
            border=ft.border.all(1, ft.colors.BLACK),  # Borda do ícone
            border_radius=size / 2,  # Borda arredondada
            bgcolor=ft.colors.WHITE,  # Fundo do ícone em branco
        )

    def on_chart_event(self, e):
        # Função que é chamada quando um evento acontece no gráfico
        for idx, section in enumerate(self.content.sections):
            if idx == e.section_index:  # Se for a seção que foi clicada
                section.radius = self.hover_radius  # Aumenta o tamanho da seção
                section.title_style = self.hover_title_style  # Altera o estilo do título
            else:
                section.radius = self.normal_radius  # Mantém o tamanho normal
                section.title_style = self.normal_title_style  # Mantém o estilo normal
        self.content.update()  # Atualiza o gráfico

class GraphFour(ft.Container):
    def __init__(self):
        super().__init__(**style_frame)

        # Definindo bordas e estilo padrão
        self.normal_border = ft.BorderSide(2, ft.colors.with_opacity(0.5, ft.colors.WHITE))  # Borda padrão
        self.hover_border = ft.BorderSide(3, ft.colors.WHITE)  # Borda ao passar o mouse
        self.radius = 80  # Tamanho das fatias do gráfico
        self.normal_title_style = ft.TextStyle(
            size=16, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD  # Estilo do título reduzido
        )
        
        # Estilo do título no hover
        self.hover_title_style = ft.TextStyle(
            size=20, color=ft.colors.YELLOW, weight=ft.FontWeight.BOLD,  # Aumenta o tamanho e muda a cor
            shadow=ft.BoxShadow(blur_radius=4, color=ft.colors.BLACK)  # Adiciona sombra
        )
        
        # Cores para cada fatia
        cores = [
            ft.colors.ORANGE,
            ft.colors.GREEN,
            ft.colors.RED,
            ft.colors.PINK,
            ft.colors.BLUE  # Adiciona a quinta cor
        ]
        
        # Cálculo do total de salários e definição de nomes
        salario_total = sum(salarios)  # Soma total dos salários

        # Criamos as fatias do gráfico com base nos salários e nomes
        sections = [
            ft.PieChartSection(
                (salario / salario_total) * 100,  # Calcula a porcentagem de cada salário
                title=f"{(salario / salario_total) * 100:.1f}%",  # Exibe a porcentagem no título
                title_position=0.7,  # Posição do título na fatia
                title_style=self.normal_title_style,  # Estilo do título
                color=cores[i],  # Define a cor da fatia
                radius=self.radius,  # Tamanho da fatia
                border_side=self.normal_border,  # Borda padrão
            )
            for i, salario in enumerate(salarios)  # Cria uma fatia para cada salário
        ]
        
        # Cria a legenda ao lado do gráfico com nome e cor
        self.legend = ft.Column(
            [
                ft.Row(
                    [
                        ft.Container(
                            width=15,
                            height=15,
                            bgcolor=cores[i % len(cores)],
                            border_radius=3,
                            border=ft.border.all(0.5, ft.colors.BLACK),
                            margin=5,
                        ),
                        ft.Text(f"{nome}", size=12, color=ft.colors.WHITE),  # Exibe apenas o nome
                    ]
                )
                for i, nome in enumerate(nomes)
            ] + [
                ft.Text(f"Total dos salários: R$ {salario_total:,.2f}", size=12, color=ft.colors.WHITE)  # Exibe o total de salários
            ]
        )

        # Adiciona o gráfico e a legenda lado a lado
        self.content = ft.Row(
            controls=[
                ft.PieChart(
                    sections=sections,
                    sections_space=6,  # Espaço entre as fatias
                    center_space_radius=0,  # Sem espaço central
                    on_chart_event=self.on_chart_event,  # Ação ao passar o mouse
                    expand=True,  # Expande para preencher o espaço
                ),
                self.legend,  # Adiciona a legenda
            ],
            alignment=ft.MainAxisAlignment.START,  # Alinha os itens na row
            spacing=10  # Espaço entre o gráfico e a legenda
        )

    def on_chart_event(self, e: ft.PieChartEvent):
        # Muda a borda e o estilo do título da fatia ao passar o mouse
        pie_chart = self.content.controls[0]  # Acessa o gráfico de pizza
        for idx, section in enumerate(pie_chart.sections):  # Acessa as seções do gráfico
            if idx == e.section_index:
                section.border_side = self.hover_border  # Borda mais grossa
                section.title_style = self.hover_title_style  # Estilo de título em hover
            else:
                section.border_side = self.normal_border  # Borda padrão
                section.title_style = self.normal_title_style  # Estilo padrão
        pie_chart.update()  # Atualiza o gráfico para aplicar as alterações


class GraphFive(ft.Container):
    def __init__(self):
        super().__init__(**style_frame)
        self.normal_border = ft.BorderSide(2, ft.colors.with_opacity(0.05, ft.colors.BLACK))
        self.hover_border = ft.BorderSide(2, ft.colors.WHITE)
        self.normal_title_style = ft.TextStyle(
            size=16, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD
        )
        self.normal_radius = 50

        # Calcula o salário total
        total_salario = sum(salarios)
        
        # Mapeia cores específicas para cada fatia/pessoa
        cores = [ft.colors.YELLOW, ft.colors.CYAN, ft.colors.PURPLE, ft.colors.CYAN_ACCENT, ft.colors.RED]

        # Cria as seções do gráfico com porcentagem do salário
        self.chart = ft.PieChart(
            sections=[
                ft.PieChartSection(
                    salario / total_salario * 100,  # Porcentagem
                    title=f"{salario / total_salario * 100:.0f}%",  # Exibe apenas a porcentagem
                    title_style=self.normal_title_style,
                    color=cores[i % len(cores)],  # Cor da fatia
                    radius=self.normal_radius,
                    border_side=self.normal_border,
                )
                for i, salario in enumerate(salarios)
            ],
            sections_space=2,
            center_space_radius=40,
            on_chart_event=self.on_chart_event,
            expand=True
        )

        # Cria a legenda ao lado do gráfico com nome e cor
        self.legend = ft.Column(
            [
                ft.Row(
                    [
                        ft.Container(
                            width=15,
                            height=15,
                            bgcolor=cores[i % len(cores)],
                            border_radius=3,
                            border=ft.border.all(0.5, ft.colors.BLACK),
                            margin=5,
                        ),
                        ft.Text(f"{nome}", size=12, color=ft.colors.WHITE),  # Exibe apenas o nome
                    ]
                )
                for i, nome in enumerate(nomes)
            ] + [
                ft.Text(f"Total de funcionários: {len(nomes)}", size=12, color=ft.colors.WHITE)
            ]
        )

        # Adiciona o gráfico e a legenda lado a lado
        self.content = ft.Row([self.chart, self.legend])

    def on_chart_event(self, e: ft.PieChartEvent):
        # Mantém o hover ajustando a borda e ampliando o título da seção destacada
        for idx, section in enumerate(self.chart.sections):
            section.border_side = (
                self.hover_border if idx == e.section_index else self.normal_border
            )
            section.title_style = ft.TextStyle(
                size=20 if idx == e.section_index else 16,  # Aumenta o título da seção em hover
                color=ft.colors.BLACK,
                weight=ft.FontWeight.BOLD
            )
        self.chart.update()  # Atualiza o gráfico para aplicar o efeito de hover


graph_one: ft.Container = GraphOne()
graph_two: ft.Container = GraphTwo()
graph_three: ft.Container = GraphThree()
graph_four: ft.Container = GraphFour()
graph_five: ft.Container = GraphFive()


def main(page: ft.Page):
    page.bgcolor = 'black'
    page.padding = 10
    page.window.maximized = True 
    page.add(
        ft.Row(
            expand=True,
            controls=[
                ft.Column(
                    expand=True,
                    controls=[graph_one, graph_two],
                ),
                ft.Column(
                    expand=True,
                    controls=[graph_three, graph_four, graph_five],
                )
            ]   
        )
    )

ft.app(target=main)
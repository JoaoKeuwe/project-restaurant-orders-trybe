import csv

from src.track_orders import TrackOrders


def analyze_log(path_to_file):
    if not str(path_to_file).endswith('.csv'):
        raise FileNotFoundError(f"Extensão inválida: {path_to_file}")
    try:
        with open(path_to_file, encoding="utf8") as arquivo:
            reader = csv.reader(
                arquivo, delimiter=",", quotechar='"'
            )
            *data, = reader
        order = TrackOrders()
        for client, food, day in data:
            order.add_new_order(client, food, day)
        response1 = order.get_most_ordered_dish_per_customer("maria")
        response2 = order.get_order_per_customer("arnaldo", "hamburguer")
        response3 = order.get_never_ordered_per_customer("joao")
        response4 = order.get_days_never_visited_per_customer("joao")
        with open("data/mkt_campaign.txt", mode="w") as file:
            file.write(
                f'{response1}\n{response2}\n{response3}\n{response4}'
            )
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: {path_to_file}")
    # refazendo o projeto diferente pois da outra maneira não passava
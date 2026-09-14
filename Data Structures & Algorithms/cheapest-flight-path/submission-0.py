class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for _ in range(k + 1):
            next_prices = prices.copy()

            for source, destination, cost in flights:
                if prices[source] == float("inf"):
                    continue

                new_price = prices[source] + cost

                if new_price < next_prices[destination]:
                    next_prices[destination] = new_price

            prices = next_prices

        return -1 if prices[dst] == float("inf") else prices[dst]
        
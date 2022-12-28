SEPARATOR = "-----"
DEFAULT_INPUT_FILE = 'deals.txt'
DEFAULT_OUTPUT_FILE = 'out.txt'


class StrategyDeal:

    @staticmethod
    def parse_text_data(data: str):
        data.replace("USD", "")
        text_deals = data.split(SEPARATOR)
        ans = []
        for text_deal in text_deals:

            bank_str_idx = text_deal.find('Bank:')
            bank_str_idx_end = text_deal.find('\n', bank_str_idx)
            entry_str_idx = text_deal.find('Entry:')
            entry_str_idx_end = text_deal.find('\n', entry_str_idx)
            target_str_idx = text_deal.find('Target:')
            target_str_idx_end = text_deal.find('\n', target_str_idx)
            close_str_idx = text_deal.find('Close:')
            close_str_idx_end = text_deal.find('\n', close_str_idx)

            bank = float(text_deal[bank_str_idx + 5:bank_str_idx_end])
            entry = float(text_deal[entry_str_idx + 6:entry_str_idx_end])
            targets_tmp = text_deal[target_str_idx + 7:target_str_idx_end].split(';')
            targets = [float(t) for t in targets_tmp]
            close = float(text_deal[close_str_idx + 6:close_str_idx_end])

            ans.append(StrategyDeal(bank, entry, targets, close))

        return ans

    def __init__(self, bank, entry, targets, close):
        self.bank = bank
        self.entry = entry
        self.targets = targets
        self.close = close

    def get_targets(self):
        # вернуть список таргетов в виде числовых значений float [21.5, 22.8, 23.5]
        pass

    def get_target_percents(self):
        # вернуть список процентов, как в примере, округленные до 3 знака [6.912, 13.376, 16.857]
        pass

    def get_target_banks(self):
        # список значений банков, если продавать активы по таргетам, как в пример, округленные до 3 знака [1069.12, 1133.764, 1168.573]
        pass

    def __str__(self):
        s_header = f"""BANK: {self.bank}
START_PRICE: {self.entry}
STOP_PRICE: {self.close}
STOP_PERCENT: {((self.entry - self.close) - 1) * 100}
STOP_BANK: {self.bank/self.entry*self.close}


1 target: 21.5432423
Percent: 7.101% # процент рассчитывается, как отношение таргета к цене входа: 21.5 / 20.11 и округляется до 3 знака
Bank: 1071.01 # величина банка, если мы продадим все активы по цене первого таргета: 1000 * 6.912 и округляется до 3 знака

2 target: 22.864732843
Percent: 13.376% # процент рассчитывается, как отношение таргета к цене входа: 22.8 / 20.11 и округляется до 3 знака
Bank: 1133.764

3 target: 23.5 # процент рассчитывается, как отношение таргета к цене входа: 23.5 / 20.11 и округляется до 3 знака
Percent: 16.857%
Bank: 1168.573
        """
        s = s_header + ""
        return s


def read_data(file_name=DEFAULT_INPUT_FILE):
    with open(file_name) as f:
        return f.read()


def write_data(data, file_name=DEFAULT_OUTPUT_FILE):
    with open(file_name, 'w') as f:
        out = f'{SEPARATOR}\n'.join([deal.__str__() for deal in data])
        f.write(out)


def main():
    pass


if __name__ == '__main__':
    main()

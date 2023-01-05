SEPARATOR = "-----"
DEFAULT_INPUT_FILE = 'deals.txt'
DEFAULT_OUTPUT_FILE = 'out.txt'


class StrategyDeal:

    @staticmethod
    def parse_text_data(data: str):
        data = data.replace("USD", "")
        text_deals = data.split(SEPARATOR)
        ans = []
        for text_deal in text_deals:

            bank_str_idx = text_deal.find('Bank:')
            if bank_str_idx == -1:
                continue
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
        return self.targets

    def get_target_percents(self):
        ans = []
        for t in self.targets:
            ans.append(round(((t / self.entry) - 1) * 100, 3))
        return ans

    def get_target_banks(self):
        ans = []
        for t in self.targets:
            ans.append(round(self.bank/self.entry*t, 3))
        return ans

    def __str__(self):
        s_header = f"""BANK: {self.bank}
START_PRICE: {self.entry}
STOP_PRICE: {self.close}
STOP_PERCENT: {round(((self.close / self.entry) - 1) * 100, 3)}%
STOP_BANK: {self.bank/self.entry*self.close}

"""
        target_text = []
        for idx, t in enumerate(self.targets):
            target_str = f"""{idx + 1} target: {t}
Percent: {round(((t / self.entry) - 1) * 100, 3)}% 
Bank: {round(self.bank/self.entry*t, 3)} 

"""
            target_text.append(target_str)
        return s_header + "".join(target_text)


def read_data(file_name=DEFAULT_INPUT_FILE):
    with open(file_name) as f:
        return f.read()


def write_data(data: list, file_name=DEFAULT_OUTPUT_FILE):
    with open(file_name, 'w') as f:
        out = f'{SEPARATOR}\n'.join([deal.__str__() for deal in data])
        f.write(out)


def main():
    data = read_data()
    deals = StrategyDeal.parse_text_data(data)
    write_data(deals)


if __name__ == '__main__':
    main()

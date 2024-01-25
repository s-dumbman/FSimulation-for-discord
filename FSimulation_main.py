from time import sleep
from keyboard import *
import random
import string
import FSimulation_info;print(FSimulation_info.version);sleep(3)
def generate_random_string(length):
    characters = string.ascii_letters
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string
random_string = generate_random_string(6)
valueable = {
    "변동수": {"value": 10},
    "변동값": {"value": 10000},
    "딜레이": {"value": 3}
}
eventable = {
    "확률성장": {"active": False, "duration": 0},
    "확률감소": {"active": False, "duration": 0}
}
playerable = {
    "테스트1": {"coin": 10000, "pCoin" : 0, "U": 0, "D": 0, "Streak": 0, "B_Streak": 0},
    "테스트2": {"coin": 10000, "pCoin" : 0, "U": 0, "D": 0, "Streak": 0, "B_Streak": 0}
}
def index():
    # --
    v = valueable["변동수"]["value"];p = valueable["변동값"]["value"];de = valueable["딜레이"]["value"];previous_player = 0
    write(f"```🖥️ 장 시작 🖥️ ({random_string}{p}-{v})```");press('enter')
    def wr(player, k, h):
        current_value = playerable[player]["coin"]
        previous_value = playerable[player]["pCoin"]
        if previous_value == 0:
            L = f"{k}₩"
        else:
            L = f"{round((abs(k) / abs(previous_value)) * 100, 1)}%"
        if current_player["Streak"] >= 1:
            if v / 4 <= valueable["변동수"]["value"] / 16:
                if h == "T":
                    write(
                        f"📈 `{player} (이)가 {L}만큼 상승하였습니다` 🔥`{current_player['Streak']+1}연속` 🕖`종료까지 {v+1}번 남음` ```유효 값어치: {round(current_value) - k}₩ => {round(current_value)}₩ (+{k}₩)```", 0, True, None)
                if h == "F":
                    write(
                        f"📉 `{player} (이)가 {L}만큼 하락하였습니다` 🔥`{current_player['Streak']+1}연속` 🕖`종료까지 {v+1}번 남음` ```유효 값어치: {round(current_value) + k}₩ => {round(current_value)}₩ (-{k}₩)```", 0, True, None)
            else:
                if h == "T":
                    write(
                        f"📈 `{player} (이)가 {L}만큼 상승하였습니다` 🔥`{current_player['Streak']+1}연속` ```유효 값어치: {round(current_value) - k}₩ => {round(current_value)}₩ (+{k}₩)```", 0, True, None)
                if h == "F":
                    write(
                        f"📉 `{player} (이)가 {L}만큼 하락하였습니다` 🔥`{current_player['Streak']+1}연속` ```유효 값어치: {round(current_value) + k}₩ => {round(current_value)}₩ (-{k}₩)```", 0, True, None)
        else:
            if v / 4 <= valueable["변동수"]["value"] / 16:
                if h == "T":
                    write(
                        f"📈 `{player} (이)가 {L}만큼 상승하였습니다` 🕖`종료까지 {v+1}번 남음` ```유효 값어치: {round(current_value) - k}₩ => {round(current_value)}₩ (+{k}₩)```", 0, True, None)
                if h == "F":
                    write(
                        f"📉 `{player} (이)가 {L}만큼 하락하였습니다` 🕖`종료까지 {v+1}번 남음` ```유효 값어치: {round(current_value) + k}₩ => {round(current_value)}₩ (-{k}₩)```", 0, True, None)
            else:
                if h == "T":
                    write(
                        f"📈 `{player} (이)가 {L}만큼 상승하였습니다` ```유효 값어치: {round(current_value) - k}₩ => {round(current_value)}₩ (+{k}₩)```", 0, True, None)
                if h == "F":
                    write(
                        f"📉 `{player} (이)가 {L}만큼 하락하였습니다` ```유효 값어치: {round(current_value) + k}₩ => {round(current_value)}₩ (-{k}₩)```", 0, True, None)
        press('enter')

    while v > 0:
        v -= 1
        per = random.choice(["true", "false"])
        ru = round(random.uniform(0, p))
        if random.random() < 0.05 and not eventable["확률성장"]["active"] and not eventable["확률감소"]["active"]:
            r = random.randint(2, 11)
            eventable["확률성장"]["active"] = True
            eventable["확률성장"]["duration"] = r
            write("```🚀 확률성장 이벤트 시작 🚀```", 0, True, None)
            press('enter')
        if random.random() < 0.05 and not eventable["확률감소"]["active"] and not eventable["확률성장"]["active"]:
            r = random.randint(2, 11)
            eventable["확률감소"]["active"] = True
            eventable["확률감소"]["duration"] = r
            write("```🔻 확률감소 이벤트 시작 🔻```", 0, True, None)
            press('enter')
        for event_name, event in eventable.items():
            if event["duration"] > 0:
                if event_name == "확률성장" and event["duration"] == 0 and event["active"]:
                    event["active"] = False
                    write(f"```🛑 {event_name} 이벤트 종료 🛑 ({round(r)-1}번 지속)```", 0, True, None)
                    press('enter')
                if event_name == "확률감소" and event["duration"] == 0 and event["active"]:
                    event["active"] = False
                    write(f"```🛑 {event_name} 이벤트 종료 🛑 ({round(r)-1}번 지속)```", 0, True, None)
                    press('enter')
        if eventable["확률성장"]["active"]:
            per = random.choice(["true", "true", "true", "true", "false"])
            ru = round(random.randint(1, p))
            eventable["확률성장"]["duration"] -= 1
            if eventable["확률성장"]["duration"] == 0:
                eventable["확률성장"]["active"] = False
                write(f"```🛑 확률성장 이벤트 종료 🛑 ({round(r)-1}번 지속)```", 0, True, None)
                press('enter')
        if eventable["확률감소"]["active"]:
            per = random.choice(["true", "false", "false", "false", "false"])
            ru = round(random.uniform(0, p))
            eventable["확률감소"]["duration"] -= 1
            if eventable["확률감소"]["duration"] == 0:
                eventable["확률감소"]["active"] = False
                write(f"```🛑 확률감소 이벤트 종료 🛑 ({round(r)-1}번 지속)```", 0, True, None)
                press('enter')
        player = random.choice(list(playerable.keys()))
        sleep(de);current_player = playerable[player]
        if previous_player == current_player:
            current_player["Streak"] += 1
        else:
            current_player["Streak"] = 0
        if per == "true":
            current_player["coin"] += ru
            current_player["U"] += 1
            wr(player, ru, "T")
        else:
            current_player["coin"] -= ru
            current_player["D"] += 1
            wr(player, ru, "F")
        previous_player = current_player
        current_player["pCoin"] = current_player["coin"]
        if current_player["Streak"]>=current_player["B_Streak"]:
            current_player["B_Streak"] = current_player["Streak"]
    sorted_players = sorted(playerable, key=lambda x: playerable[x]["coin"], reverse=True)
    rank = 1
    write(f"```🏆 순위 집계 🏆 ({random_string}{p}-{v})```", 0, True, None)
    # --
    for player in sorted_players:
        coin_value = playerable[player]["coin"]
        U_value = playerable[player]["U"]
        D_value = playerable[player]["D"]
        BestSt = playerable[player]["B_Streak"]
        if coin_value >= 0:
            write(f"`{rank}위: {player} - {round(coin_value)}₩` ```📈{U_value} / 📉{D_value} / 🔥{BestSt+1}```", 0, True, None)
        elif coin_value < 0:
            write(f"💀`: {player} - 파산 ({-round(coin_value)}₩ 적자)` ```📈{U_value} / 📉{D_value} / 🔥{BestSt+1}```", 0, True, None)
        press('enter')
        sleep(1)
        rank += 1
    # --
if __name__=='__main__':
    index()
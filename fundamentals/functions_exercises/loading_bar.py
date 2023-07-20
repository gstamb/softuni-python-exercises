def display_load_bar(progress: int) -> str:
    tot = 10
    on = progress // 10
    off = tot - on

    bar = f"[{on * '%'}{off * '.'}]"
    return bar

current_progress = int(input())
if current_progress//10 < 10:
    z = f"{current_progress}% {display_load_bar(current_progress)}\nStill loading..."
    print(z)
else:
    print("100% Complete!")
    print(f"{display_load_bar(current_progress)}")

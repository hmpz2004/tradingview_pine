//@version=3
study("MA_CROSS_AREA")

k_cnt = input('300', type=integer, title="均线交叉区间k线最大个数")

total_area = 0.0
distance = 0

cur_ma5 = sma(close, 5)
cur_ma10 = sma(close, 10)
status_bull = (cur_ma5 > cur_ma10 ? true : false)
//status_bull = true
item_ma5 = 0.0
item_ma10 = 0.0

for i = 0 to k_cnt
    need_break = false
    
    item_ma5 := sma(close[i], 5)
    item_ma10 := sma(close[i], 10)
    if status_bull
        // 多头
        if item_ma5 < item_ma10
            need_break := true
        else
            distance := distance+1
            total_area := total_area + item_ma5 - item_ma10
    else
        // 空头
        if item_ma5 > item_ma10
            need_break := true
        else
            distance := distance+1
            total_area := total_area + item_ma10 - item_ma5
    if need_break
        // distance
        break

// plot(total_area)
plot(distance)

// debug_1
// p = 0.2
// if status_bull
//     p := 0.6
// else
//     p := 0.3
// plot(p)
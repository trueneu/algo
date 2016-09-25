f = open('cookies_input.txt')

#n, k = [int(x) for x in input().strip().split()]
n, k = [int(x) for x in f.readline().strip().split()]

#cookies = [int(x) for x in input().strip().split()]
cookies = sorted([int(x) for x in f.readline().strip().split()])

q = list()

iterations = 0
not_possible = False

cookie_i = 0
q_i = 0
while (cookies[cookie_i] < k if cookie_i < len(cookies) else False) or (q[q_i] < k if q_i < len(q) else False):
    if cookie_i < len(cookies) and q_i < len(q):
        if cookies[cookie_i] < q[q_i]:
            if len(cookies) - cookie_i > 1 and cookies[cookie_i + 1] < q[q_i]:
                cookie1 = cookies[cookie_i]
                cookie_i += 1
                cookie2 = cookies[cookie_i]
                cookie_i += 1
            else:
                cookie1 = cookies[cookie_i]
                cookie_i += 1
                cookie2 = q[q_i]
                q_i += 1
        else:
            if len(q) - q_i > 1 and q[q_i + 1] < cookies[cookie_i]:
                cookie1 = q[q_i]
                q_i += 1
                cookie2 = q[q_i]
                q_i += 1
            else:
                cookie1 = q[q_i]
                q_i += 1
                cookie2 = cookies[cookie_i]
                cookie_i += 1
    elif cookie_i < len(cookies):
        if len(cookies) - cookie_i > 1:
            cookie1 = cookies[cookie_i]
            cookie_i += 1
            cookie2 = cookies[cookie_i]
            cookie_i += 1
        else:
            not_possible = True
            break
    elif q_i < len(q):
        if len(q) - q_i > 1:
            cookie1 = q[q_i]
            q_i += 1
            cookie2 = q[q_i]
            q_i += 1
        else:
            not_possible = True
            break
    else:
        not_possible = True
        break

    cookie = cookie1 + 2 * cookie2
    q.append(cookie)

    iterations += 1

if not_possible:
    print(-1)
else:
    print(iterations)

    
            

                
                                
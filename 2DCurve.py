import pygame as pg

lut = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1]]

def Binominal(n, k):   #C_n^k = n!/k!*(n-k)!
    nextRow = []
    while (n >= len(lut)):
        s = len(lut)
        nextRow[0] = 1;
        for i in range(1, s):
            pres = s - 1
            nextRow[i] = (lut[pres][i - 1] + lut[pres][i])
        nextRow[s] = 1
        lut.append(nextRow)
    return lut[n][k]

def Bezier(n, t, w, r):
    sum = 0
    basis = 0
    for k in range (0, n):
        basis += Binominal(n - 1, k) * ((1 - t) ** \
                                      (n - 1 - k)) * (t ** k) * r[k]
    for k in range (0, n):
        sum += Binominal(n - 1, k) * ((1 - t) ** \
                                      (n - 1 - k)) * (t ** k) * w[k] * r[k]
    return sum / basis

def Bezier2(t, w, r):
    t2 = t * t
    mt = 1 - t
    mt2 = mt * mt
    f = [r[0] * mt2, 2 * r[1] * mt * t, r[2] * t2] #Implement
    basis = f[0] + f[1] + f[2] #Implement
    return (f[0] * w[0] + f[1] * w[1] + f[2] * w[2]) / basis
    #return w[0] * mt2 + w[1] * 2 * mt * t + w[2] * t2

def Bezier3(t,w, r):
    t2 = t * t
    t3 = t2 * t
    mt = 1-t
    mt2 = mt * mt
    mt3 = mt2 * mt
    f = [r[0] * mt3, 3 * r[1] * mt2 * t, 3 * r[2] * mt * t2, r[3] * t3] #Implement
    basis = f[0] + f[1] + f[2] + f[3] #Implement
    return (f[0] * w[0] + f[1] * w[1] + f[2] * w[2] + f[3] * w[3])/basis
    #return w[0]*mt3 + 3*w[1]*mt2*t + 3*w[2]*mt*t2 + w[3]*t3



# Creating a pygame window
pg.init()
screen = pg.display.set_mode((600, 400))
pg.display.set_caption('Bezier Curve')

# The main cycle
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Clearing the screen
    screen.fill((255, 255, 255))

    # Weights
    #weight = [(110, 150), (25, 190), (210, 250), (210, 30)]
    #weight = [(141, 59), (47, 64), (50, 241), (161, 114)]
    weight = [(30, 60), (180, 55), (30, 192), (219, 223)]
    ratio = [0.16, 1.23, 1.39, 0.24]
    points = []

    # Building a Bezier curve
    for t in range(0, 101):
        t_normalized = t / 100
        x = Bezier(len(weight), t_normalized, [p[0] for p in weight], ratio)
        y = Bezier(len(weight), t_normalized, [p[1] for p in weight], ratio)
        #x = Bezier3(t_normalized, [p[0] for p in control_points])
        #y = Bezier3(t_normalized, [p[1] for p in control_points])
        #pg.draw.circle(screen, (0, 0, 255), (int(x), int(y)), 2)

        # Adding the current point to the list
        points.append((int(x), int(y)))

        # Adding a line between the current and previous point
        if len(points) > 1:
            pg.draw.lines(screen, (83,55,122), False, points, width=3)

    # Displaying control points
    for point in weight:
        pg.draw.circle(screen, (255,207,64), point, 5)

    pg.display.flip()

# Ending the pygame program
pg.quit()
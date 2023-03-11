def triangulation(polygon, epsilon = 10**(-12)):

    if not strictly_y_monotone(polygon):
        return

    points = [] # przechowuje punkty w postaci (x,y,'l'/'r'/'b') l- lewy łańcuch r- prawy b- należy do obu
    highest_id = 0
    lowest_id = 0
    if polygon.points == []:
        print("Coś poszło nie tak podczas wczytywania wielokąta z wykresu (Wina narzędzia graficznego). Spróbuj narysować go ponowanie.")
        return

    # Znajduje najwyższy i najniższy punkt
    for (i,p) in enumerate(polygon.points):
        if p[1] > polygon.points[highest_id][1]:
            highest_id = i
        if p[1] < polygon.points[lowest_id][1]:
            lowest_id = i

    points.append(Tri_point(polygon.points[highest_id][0], polygon.points[highest_id][1], 'b',
                            polygon.points[(highest_id -1 )% len(polygon.points)],
                            polygon.points[(highest_id +1 )% len(polygon.points)]))



    l_id = highest_id + 1
    r_id = highest_id - 1

    # dodaje wyższy z punktów i przypisuje mu symbol łańcucha, działa podobnie jak merge z mergesort
    while polygon.points[l_id % len(polygon.points)] is not polygon.points[lowest_id] and polygon.points[r_id % len(polygon.points)] is not polygon.points[lowest_id]:

        if polygon.points[l_id % len(polygon.points)][1] > polygon.points[r_id % len(polygon.points)][1]:
            tmp_id = l_id % len(polygon.points)
            points.append(Tri_point(polygon.points[tmp_id][0], polygon.points[tmp_id][1], 'l',
                                    polygon.points[(tmp_id -1) % len(polygon.points)],
                                    polygon.points[(tmp_id +1)% len(polygon.points)]))
            l_id += 1
        else:
            tmp_id = r_id % len(polygon.points)
            points.append(Tri_point(polygon.points[tmp_id][0], polygon.points[tmp_id][1], 'r',
                                    polygon.points[(tmp_id -1) % len(polygon.points)],
                                    polygon.points[(tmp_id +1) % len(polygon.points)]))
            r_id -= 1

    # jeśli w jakimś łańcuchu są jeszcze nieprzejrzane punkty to zostają dodane
    while polygon.points[l_id % len(polygon.points)] is not polygon.points[lowest_id]:
        tmp_id = l_id % len(polygon.points)
        points.append(Tri_point(polygon.points[tmp_id][0], polygon.points[tmp_id][1], 'l',
                                polygon.points[(tmp_id -1) % len(polygon.points)],
                                polygon.points[(tmp_id +1) % len(polygon.points)]))
        l_id += 1

    while polygon.points[r_id % len(polygon.points)] is not polygon.points[lowest_id]:
        tmp_id = r_id % len(polygon.points)
        points.append(Tri_point(polygon.points[tmp_id][0], polygon.points[tmp_id][1], 'r',
                                polygon.points[(tmp_id -1) % len(polygon.points)],
                                polygon.points[(tmp_id +1) % len(polygon.points)]))
        r_id -= 1

    points.append(Tri_point(polygon.points[lowest_id][0], polygon.points[lowest_id][1], 'b',
                            polygon.points[(lowest_id -1) % len(polygon.points)],
                            polygon.points[(lowest_id +1) % len(polygon.points)]))

    # Przeglądanie posortowanych punktów
    stack = []
    stack.append(points[0])
    stack.append(points[1])
    scenes=[(Scene([PointsCollection(polygon.points , color = "black"),
                    PointsCollection(stack_to_points(stack) , color = "red")],
                   [LinesCollection(to_lines(polygon.points) + [(polygon.points[-1], polygon.points[0])], color = "black")]))]

    lines = []
    for i in range(2, len(points)-1):
        curr = points[i]

        # Jeśli punkty należą do innego łańcucha
        if curr.chain != stack[-1].chain:
            for v in stack:
                if (not v.are_neighbours(curr)):
                    lines.append(((v.x,v.y),(curr.x,curr.y)))
                    stack = [points[i-1], points[i]]
                    add_scenes(scenes,polygon, stack, lines)

        # Jeśli punkty należą do tego samego łańcucha
        else:
            j = len(stack) -1
            while j > 0:
                scenes.append(Scene([PointsCollection(polygon.points , color = "black"),
                                     PointsCollection(stack_to_points(stack) , color = "red"),
                                     PointsCollection([(curr.x, curr.y),(stack[j-1].x, stack[j-1].y),(stack[j].x, stack[j].y)], color = "blue")],
                                    [LinesCollection(to_lines(polygon.points) +[(polygon.points[-1], polygon.points[0])], color = "black"),
                                     LinesCollection(lines.copy(), color = "orange")]))


                if  triangle_in_polygon(stack[j-1], stack[j], curr, epsilon):
                    if not curr.are_neighbours(stack[j-1]):
                        lines.append(((curr.x, curr.y),(stack[j-1].x, stack[j-1].y)))
                        stack.pop(len(stack) -1)
                    j -= 1
                else:
                    j=-1
            stack.append(curr)
            add_scenes(scenes,polygon, stack, lines)

    for p in stack:
        if not p.are_neighbours(points[len(points) -1]):
            lines.append(((points[len(points) -1].x, points[len(points) -1].y),(p.x,p.y)))

    stack = []
    add_scenes(scenes,polygon, stack, lines)
    return (lines, scenes)

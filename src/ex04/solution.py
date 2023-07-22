def solution(groups: list[int], auditories: list[int]) -> int:
    groups.sort()
    auditories.sort()

    position = 0
    answer = 0

    for group in groups:
        
        while position < len(auditories) and auditories[position] < group:
            position += 1

        if position != len(auditories):
            answer += 1
            position += 1

    return answer


if __name__ == "__main__":
    number_of_groups = int(input())
    groups = list(map(int, input().split()))

    number_of_auditories = int(input())
    auditories = list(map(int, input().split()))

    print(solution(groups, auditories))




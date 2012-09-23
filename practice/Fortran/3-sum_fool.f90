program test
    INTEGER :: i,j,k,n,count
    INTEGER, ALLOCATABLE:: mas(:)

    OPEN(unit=12, file="../tests/8d Kint.txt")

    READ(12, *) n
    ALLOCATE(mas(n))

    READ(12, *) mas

    count = 0
    DO i=1,n-2
        DO j = i+1, n-1
            DO k = j+1, n
                IF (mas(i) + mas(j) + mas(k) == 0) THEN
                    count = count + 1
                END IF
            END DO
        END DO
    END DO

    print *, count
    DEALLOCATE(mas)
end
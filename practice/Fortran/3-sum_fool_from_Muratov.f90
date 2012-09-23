program test

    implicit none

    integer :: i, j, k, n, count, ai, aj

    integer, allocatable :: mas(:)

    real(8) start, finish

    open(unit = 12, file = '../tests/8Kint.txt')

    read(12, *) n

    allocate(mas(n))

    read(12, *) mas

    count = 0

    call cpu_time(start)

    do i = 1, (n - 2)

ai = mas(i)

do j = (i + 1), (n - 1)

aj = ai + mas(j)

do k = (j + 1), n

if ( aj + mas(k) == 0 ) count = count + 1

enddo

enddo

enddo

    call cpu_time(finish)

    print *, count

    print *, 'Total time taken by CPU:', finish - start

    deallocate(mas)

end

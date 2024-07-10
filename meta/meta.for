!dir$ freeform
!===============================================================================
! Desc: uexternaldb and umat for one element test
! Code by: libofeng, contact info: bf_li@qq.com
! Date: 2024-07-10
!===============================================================================
!
! include 'utils.f90'
! 
!!$ User subroutine to manage user-defined external databases and 
!!$ calculate model-independent history information.
subroutine uexternaldb(lop, lrestart, time, dtime, kstep, kinc)
    !-------------------------------------------------------------------------80
    implicit none
    integer(kind=4), intent(in) :: lop, lrestart, kstep, kinc
    real(kind=8), intent(in) :: time(2), dtime(1)
    !---------------------------------------------------------------------------
    if (lop==0) then
        write(*,*) "lop: ", lop
        write(*,*) "time: ", time
        write(*,*) "dtime: ", dtime
        write(*,*) "kstep: ", kstep
        write(*,*) "kinc: ", kinc
        write(*,*) "-----------------------------------------------------------"
    end if

    if (lop==1) then
        write(*,*) "lop: ", lop
        write(*,*) "time: ", time
        write(*,*) "dtime: ", dtime
        write(*,*) "kstep: ", kstep
        write(*,*) "kinc: ", kinc
        write(*,*) "-----------------------------------------------------------"
    end if

    if (lop==2) then
        write(*,*) "lop: ", lop
        write(*,*) "time: ", time
        write(*,*) "dtime: ", dtime
        write(*,*) "kstep: ", kstep
        write(*,*) "kinc: ", kinc
        write(*,*) "-----------------------------------------------------------"
    end if

    ! write(*,*) "hello uexternaldb!"

end subroutine uexternaldb
!
!
!!$ User subroutine to define a material's mechanical behavior
subroutine umat(stress, statev, ddsdde, sse,    spd,    scd,    rpl,    ddsddt,&
    &           drplde, drpldt, stran,  dstran, time,   dtime,  temp,   dtemp, &
    &           predef, dpred,  cmname, ndi,    nshr,   ntens,  nstatv, props, &
    &           nprops, coords, drot,   pnewdt, celent, dfgrd0, dfgrd1, noel,  &
    &           npt,    layer,  kspt,   kstep,  kinc)
    !-------------------------------------------------------------------------80
    !
    !use utilies, only:
    ! 
    !-------------------------------------------------------------------------80
    !all parameters are explicitly declared to avoid potential mistakes
    !include 'aba_param.inc'
    implicit none
    integer(kind=4), parameter :: nprecd=2

    character(len=80) :: cmname
    integer(kind=4) :: ndi, nshr, ntens, nstatv, nprops, noel, npt, layer,     &
    &  kspt,  kstep, kinc
    real(kind=8) :: sse, spd, scd, rpl, drpldt, dtime, temp, dtemp, pnewdt,    &
    &  celent
    real(kind=8) :: stress(ntens), statev(nstatv), ddsdde(ntens, ntens),       &
    &  ddsddt(ntens), drplde(ntens), stran(ntens), dstran(ntens), time(2),     &
    &  predef(1), dpred(1), props(nprops), coords(3), drot(3, 3),              &
    &  dfgrd0(3, 3), dfgrd1(3, 3)
    !---------------------------------------------------------------------------
    !!$ user-define parameters
    real(kind=8) :: emod, enu, eg, ebulk, elambda
    real(kind=8), parameter :: enumax=0.499d0
    integer(kind=4) :: k1
    !---------------------------------------------------------------------------
    !!$ elastic parameters
    emod = props(1)
    enu = min(props(2),enumax)
    ebulk = emod / (3.d0 * (1.d0 -2.d0 * enu))
    eg = emod / (2.d0 * (1.d0 + enu))
    elambda = ebulk - 2.d0 / 3.d0 * eg
    !!$ iostropic elastic modulus (mandel form)
    ddsdde = 0.d0
    ddsdde(1:ndi,1:ndi) = elambda
    do k1 = 1, ndi
        ddsdde(k1, k1) = elambda + 2.d0 * eg
    end do
    do k1 = ndi+1, ntens
        ddsdde(k1,k1) = eg
    end do
    !$ elastic behavior
    stress(:) = stress(:) + matmul(ddsdde(:,:), dstran(:))

    ! write(*,*) "hello umat!"

end subroutine umat
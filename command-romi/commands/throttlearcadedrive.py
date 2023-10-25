# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.

import typing
from subsystems.drivetrain import Drivetrain
from commands.arcadedrive import ArcadeDrive


class ThrottleArcadeDrive(ArcadeDrive):
    def __init__(
        self,
        drive: Drivetrain,
        forward: typing.Callable[[], float],
        rotation: typing.Callable[[], float],
        throttle: typing.Callable[[], float],
    ) -> None:
        """Creates a new ThrottleArcadeDrive. This command will drive your robot according to the
        speed supplier lambdas. This command does not terminate.

        :param drivetrain:  The drivetrain subsystem on which this command will run
        :param forward:     Callable supplier of forward/backward speed
        :param rotation:    Callable supplier of rotational speed
        :param throttle:    Callable supplier of max speed for driving
        """
        super().__init__(drive, forward, rotation)

        self.throttle = throttle

        self.addRequirements([self.drive])

    def get_arcade_drive_values(self):
        # Grab current stick/throttle positions
        curr_throttle = self.throttle()
        fwd = self.forward()
        rot = self.rotation()
        fwd_sign = 1 if fwd > 0 else -1
        rot_sign = 1 if rot > 0 else -1
        # Square the input value to give it a curved response instead of
        # linear, then multiply by either 1 or -1 to get the correct positive
        # or negative value
        fwd = fwd**2 * fwd_sign
        rot = rot**2 * rot_sign
        # axis goes from -1 to 1 but we want a value between 0 and 1
        curr_throttle = 1 - ((curr_throttle+1)/2)
        # Now adjust the stick reading by the throttle. If throttle is at max
        # stick has full range of throttle. If throttle is at 50% pushing the
        # stick to full only produces 50% of throttle
        fwd *= curr_throttle
        print(f'Throttle: {curr_throttle:0.3f} Drive power: {fwd:0.3f} Rotation: {rot:0.3f}')
        return fwd, rot

    def execute(self) -> None:
        fwd, rot = self.get_arcade_drive_values()
        self.drive.arcadeDrive(fwd, rot)

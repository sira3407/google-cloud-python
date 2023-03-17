# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import proto  # type: ignore

from google.apps.script.type import extension_point_pb2  # type: ignore

__protobuf__ = proto.module(
    package="google.apps.script.type.calendar",
    manifest={
        "CalendarAddOnManifest",
        "ConferenceSolution",
        "CalendarExtensionPoint",
    },
)


class CalendarAddOnManifest(proto.Message):
    r"""Calendar add-on manifest.

    Attributes:
        homepage_trigger (google.apps.script.type.extension_point_pb2.HomepageExtensionPoint):
            Defines an endpoint that will be executed contexts that
            don't match a declared contextual trigger. Any cards
            generated by this function will always be available to the
            user, but may be eclipsed by contextual content when this
            add-on declares more targeted triggers.

            If present, this overrides the configuration from
            ``addOns.common.homepageTrigger``.
        conference_solution (MutableSequence[google.apps.script.type.calendar.types.ConferenceSolution]):
            Defines conference solutions provided by this
            add-on.
        create_settings_url_function (str):
            An endpoint to execute that creates a URL to
            the add-on's settings page.
        event_open_trigger (google.apps.script.type.calendar.types.CalendarExtensionPoint):
            An endpoint to trigger when an event is
            opened (viewed/edited).
        event_update_trigger (google.apps.script.type.calendar.types.CalendarExtensionPoint):
            An endpoint to trigger when the open event is
            updated.
        current_event_access (google.apps.script.type.calendar.types.CalendarAddOnManifest.EventAccess):
            Define the level of data access when an event
            addon is triggered.
    """

    class EventAccess(proto.Enum):
        r"""An enum defining the level of data access event triggers
        require.

        Values:
            UNSPECIFIED (0):
                Default value when nothing is set for
                EventAccess.
            METADATA (1):
                METADATA gives event triggers the permission
                to access the metadata of events such as event
                id and calendar id.
            READ (3):
                READ gives event triggers access to all
                provided event fields including the metadata,
                attendees, and conference data.
            WRITE (4):
                WRITE gives event triggers access to the
                metadata of events and the ability to perform
                all actions, including adding attendees and
                setting conference data.
            READ_WRITE (5):
                READ_WRITE gives event triggers access to all provided event
                fields including the metadata, attendees, and conference
                data and the ability to perform all actions.
        """
        UNSPECIFIED = 0
        METADATA = 1
        READ = 3
        WRITE = 4
        READ_WRITE = 5

    homepage_trigger: extension_point_pb2.HomepageExtensionPoint = proto.Field(
        proto.MESSAGE,
        number=6,
        message=extension_point_pb2.HomepageExtensionPoint,
    )
    conference_solution: MutableSequence["ConferenceSolution"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="ConferenceSolution",
    )
    create_settings_url_function: str = proto.Field(
        proto.STRING,
        number=5,
    )
    event_open_trigger: "CalendarExtensionPoint" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="CalendarExtensionPoint",
    )
    event_update_trigger: "CalendarExtensionPoint" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="CalendarExtensionPoint",
    )
    current_event_access: EventAccess = proto.Field(
        proto.ENUM,
        number=12,
        enum=EventAccess,
    )


class ConferenceSolution(proto.Message):
    r"""Defines conference related values.

    Attributes:
        on_create_function (str):
            Required. The endpoint to call when
            ConferenceData should be created.
        id (str):
            Required. IDs should be unique across
            ConferenceSolutions within one add-on, but this
            is not strictly enforced. It is up to the add-on
            developer to assign them uniquely, otherwise the
            wrong ConferenceSolution may be used when the
            add-on is triggered. While the developer may
            change the display name of an add-on, the ID
            should not be changed.
        name (str):
            Required. The display name of the
            ConferenceSolution.
        logo_url (str):
            Required. The URL for the logo image of the
            ConferenceSolution.
    """

    on_create_function: str = proto.Field(
        proto.STRING,
        number=1,
    )
    id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    logo_url: str = proto.Field(
        proto.STRING,
        number=6,
    )


class CalendarExtensionPoint(proto.Message):
    r"""Common format for declaring a calendar add-on's triggers.

    Attributes:
        run_function (str):
            Required. The endpoint to execute when this
            extension point is activated.
    """

    run_function: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))

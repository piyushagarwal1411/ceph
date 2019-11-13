import json

from ceph.deployment.inventory import Devices


def test_from_json():
    data = json.loads("""
    [
  {
    "available": false,
    "rejected_reasons": [
      "locked"
    ],
    "sys_api": {
      "scheduler_mode": "",
      "rotational": "0",
      "vendor": "",
      "human_readable_size": "50.00 GB",
      "sectors": 0,
      "sas_device_handle": "",
      "partitions": {},
      "rev": "",
      "sas_address": "",
      "locked": 1,
      "sectorsize": "512",
      "removable": "0",
      "path": "/dev/dm-0",
      "support_discard": "",
      "model": "",
      "ro": "0",
      "nr_requests": "128",
      "size": 53687091200
    },
    "lvs": [],
    "path": "/dev/dm-0"
  },
  {
    "available": false,
    "rejected_reasons": [
      "locked"
    ],
    "sys_api": {
      "scheduler_mode": "",
      "rotational": "0",
      "vendor": "",
      "human_readable_size": "31.47 GB",
      "sectors": 0,
      "sas_device_handle": "",
      "partitions": {},
      "rev": "",
      "sas_address": "",
      "locked": 1,
      "sectorsize": "512",
      "removable": "0",
      "path": "/dev/dm-1",
      "support_discard": "",
      "model": "",
      "ro": "0",
      "nr_requests": "128",
      "size": 33789313024
    },
    "lvs": [],
    "path": "/dev/dm-1"
  },
  {
    "available": false,
    "rejected_reasons": [
      "locked"
    ],
    "sys_api": {
      "scheduler_mode": "",
      "rotational": "0",
      "vendor": "",
      "human_readable_size": "394.27 GB",
      "sectors": 0,
      "sas_device_handle": "",
      "partitions": {},
      "rev": "",
      "sas_address": "",
      "locked": 1,
      "sectorsize": "512",
      "removable": "0",
      "path": "/dev/dm-2",
      "support_discard": "",
      "model": "",
      "ro": "0",
      "nr_requests": "128",
      "size": 423347879936
    },
    "lvs": [],
    "path": "/dev/dm-2"
  },
  {
    "available": false,
    "rejected_reasons": [
      "locked"
    ],
    "sys_api": {
      "scheduler_mode": "cfq",
      "rotational": "0",
      "vendor": "ATA",
      "human_readable_size": "476.94 GB",
      "sectors": 0,
      "sas_device_handle": "",
      "partitions": {
        "sda2": {
          "start": "411648",
          "holders": [],
          "sectorsize": 512,
          "sectors": "2097152",
          "size": "1024.00 MB"
        },
        "sda3": {
          "start": "2508800",
          "holders": [
            "dm-1",
            "dm-2",
            "dm-0"
          ],
          "sectorsize": 512,
          "sectors": "997705728",
          "size": "475.74 GB"
        },
        "sda1": {
          "start": "2048",
          "holders": [],
          "sectorsize": 512,
          "sectors": "409600",
          "size": "200.00 MB"
        }
      },
      "rev": "0000",
      "sas_address": "",
      "locked": 1,
      "sectorsize": "512",
      "removable": "0",
      "path": "/dev/sda",
      "support_discard": "",
      "model": "SanDisk SD8SN8U5",
      "ro": "0",
      "nr_requests": "128",
      "size": 512110190592
    },
    "lvs": [
      {
        "comment": "not used by ceph",
        "name": "swap"
      },
      {
        "comment": "not used by ceph",
        "name": "home"
      },
      {
        "comment": "not used by ceph",
        "name": "root"
      }
    ],
    "path": "/dev/sda"
  }
]""".strip())
    ds = Devices.from_json(data)
    assert len(ds.devices) == 4
    assert Devices.from_json(ds.to_json()) == ds

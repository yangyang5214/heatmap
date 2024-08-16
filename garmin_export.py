"""
Python 3 API wrapper for Garmin Connect to get your statistics.
Copy most code from https://github.com/cyberjunky/python-garminconnect
"""

import argparse
import asyncio
import datetime
import os
import time
import traceback
import zipfile

import garth

from garmin_secret import GarminLogin


class Garmin:
    def __init__(self, secret_path, is_cn):
        """Create a new class instance."""
        self.is_cn = is_cn

        self.garmin_connect_user_settings_url = (
            "/userprofile-service/userprofile/user-settings"
        )
        self.garmin_connect_devices_url = (
            "/device-service/deviceregistration/devices"
        )
        self.garmin_connect_device_url = "/device-service/deviceservice"

        self.garmin_connect_primary_device_url = (
            "/web-gateway/device-info/primary-training-device"
        )

        self.garmin_connect_solar_url = "/web-gateway/solar"
        self.garmin_connect_weight_url = "/weight-service"
        self.garmin_connect_daily_summary_url = (
            "/usersummary-service/usersummary/daily"
        )
        self.garmin_connect_metrics_url = (
            "/metrics-service/metrics/maxmet/daily"
        )
        self.garmin_connect_daily_hydration_url = (
            "/usersummary-service/usersummary/hydration/daily"
        )
        self.garmin_connect_set_hydration_url = (
            "usersummary-service/usersummary/hydration/log"
        )
        self.garmin_connect_daily_stats_steps_url = (
            "/usersummary-service/stats/steps/daily"
        )
        self.garmin_connect_personal_record_url = (
            "/personalrecord-service/personalrecord/prs"
        )
        self.garmin_connect_earned_badges_url = "/badge-service/badge/earned"
        self.garmin_connect_adhoc_challenges_url = (
            "/adhocchallenge-service/adHocChallenge/historical"
        )
        self.garmin_connect_badge_challenges_url = (
            "/badgechallenge-service/badgeChallenge/completed"
        )
        self.garmin_connect_available_badge_challenges_url = (
            "/badgechallenge-service/badgeChallenge/available"
        )
        self.garmin_connect_non_completed_badge_challenges_url = (
            "/badgechallenge-service/badgeChallenge/non-completed"
        )
        self.garmin_connect_inprogress_virtual_challenges_url = (
            "/badgechallenge-service/virtualChallenge/inProgress"
        )
        self.garmin_connect_daily_sleep_url = (
            "/wellness-service/wellness/dailySleepData"
        )
        self.garmin_connect_daily_stress_url = (
            "/wellness-service/wellness/dailyStress"
        )
        self.garmin_connect_hill_score_url = (
            "/metrics-service/metrics/hillscore"
        )

        self.garmin_connect_daily_body_battery_url = (
            "/wellness-service/wellness/bodyBattery/reports/daily"
        )

        self.garmin_connect_blood_pressure_endpoint = (
            "/bloodpressure-service/bloodpressure/range"
        )

        self.garmin_connect_set_blood_pressure_endpoint = (
            "/bloodpressure-service/bloodpressure"
        )

        self.garmin_connect_endurance_score_url = (
            "/metrics-service/metrics/endurancescore"
        )
        self.garmin_connect_menstrual_calendar_url = (
            "/periodichealth-service/menstrualcycle/calendar"
        )

        self.garmin_connect_menstrual_dayview_url = (
            "/periodichealth-service/menstrualcycle/dayview"
        )
        self.garmin_connect_pregnancy_snapshot_url = (
            "periodichealth-service/menstrualcycle/pregnancysnapshot"
        )
        self.garmin_connect_goals_url = "/goal-service/goal/goals"

        self.garmin_connect_rhr_url = "/userstats-service/wellness/daily"

        self.garmin_connect_hrv_url = "/hrv-service/hrv"

        self.garmin_connect_training_readiness_url = (
            "/metrics-service/metrics/trainingreadiness"
        )

        self.garmin_connect_race_predictor_url = (
            "/metrics-service/metrics/racepredictions"
        )
        self.garmin_connect_training_status_url = (
            "/metrics-service/metrics/trainingstatus/aggregated"
        )
        self.garmin_connect_user_summary_chart = (
            "/wellness-service/wellness/dailySummaryChart"
        )
        self.garmin_connect_floors_chart_daily_url = (
            "/wellness-service/wellness/floorsChartData/daily"
        )
        self.garmin_connect_heartrates_daily_url = (
            "/wellness-service/wellness/dailyHeartRate"
        )
        self.garmin_connect_daily_respiration_url = (
            "/wellness-service/wellness/daily/respiration"
        )
        self.garmin_connect_daily_spo2_url = (
            "/wellness-service/wellness/daily/spo2"
        )
        self.garmin_all_day_stress_url = (
            "/wellness-service/wellness/dailyStress"
        )
        self.garmin_connect_activities = (
            "/activitylist-service/activities/search/activities"
        )
        self.garmin_connect_activity = "/activity-service/activity"
        self.garmin_connect_activity_types = (
            "/activity-service/activity/activityTypes"
        )
        self.garmin_connect_activity_fordate = (
            "/mobile-gateway/heartRate/forDate"
        )
        self.garmin_connect_fitnessstats = "/fitnessstats-service/activity"

        self.garmin_connect_fit_download = "/download-service/files/activity"
        self.garmin_connect_tcx_download = (
            "/download-service/export/tcx/activity"
        )
        self.garmin_connect_gpx_download = (
            "/download-service/export/gpx/activity"
        )
        self.garmin_connect_kml_download = (
            "/download-service/export/kml/activity"
        )
        self.garmin_connect_csv_download = (
            "/download-service/export/csv/activity"
        )

        self.garmin_connect_upload = "/upload-service/upload"

        self.garmin_connect_gear = "/gear-service/gear/filterGear"
        self.garmin_connect_gear_baseurl = "/gear-service/gear/"

        self.garmin_request_reload_url = (
            "/wellness-service/wellness/epoch/request"
        )

        self.garmin_workouts = "/workout-service"

        self.garmin_connect_delete_activity_url = "/activity-service/activity"

        self.garth = garth.Client(
            domain="garmin.cn" if is_cn else "garmin.com"
        )

        self.garth.load(secret_path)
        if self.garth.oauth2_token.expired:
            self.garth.refresh_oauth2()

    def connectapi(self, path, **kwargs):
        return self.garth.connectapi(path, **kwargs)

    def download_activity(self, activity_id):
        url = f"/download-service/export/gpx/activity/{activity_id}"
        return self.download(url)


    def download(self, path, **kwargs):
        return self.garth.download(path, **kwargs)

    def get_activity_id_list(self):
        activities = []
        start = 0
        limit = 20
        url = self.garmin_connect_activities
        today = datetime.date.today()
        start_date = today - datetime.timedelta(days=100)
        params = {
            "startDate": str(start_date.isoformat()),
            "endDate": str(today.isoformat()),
            "start": str(start),
            "limit": str(limit),
        }
        while True:
            params["start"] = str(start)
            act = self.connectapi(url, params=params)
            if act:
                activities.extend(act)
                start = start + limit
            else:
                break
        return [str(item["activityId"]).split("_")[0]
                for item in activities
                if item['activityType']['typeKey'] != 'other'
                ]


class GarminConnectHttpError(Exception):
    def __init__(self, status):
        super(GarminConnectHttpError, self).__init__(status)
        self.status = status


class GarminConnectConnectionError(Exception):
    """Raised when communication ended in error."""

    def __init__(self, status):
        """Initialize."""
        super(GarminConnectConnectionError, self).__init__(status)
        self.status = status


class GarminConnectTooManyRequestsError(Exception):
    """Raised when rate limit is exceeded."""

    def __init__(self, status):
        """Initialize."""
        super(GarminConnectTooManyRequestsError, self).__init__(status)
        self.status = status


class GarminConnectAuthenticationError(Exception):
    """Raised when login returns wrong result."""

    def __init__(self, status):
        """Initialize."""
        super(GarminConnectAuthenticationError, self).__init__(status)
        self.status = status


def download_garmin_data(api, activity_id, folder):
    try:
        file_data = api.download_activity(activity_id)
        file_path = os.path.join(folder, f"{activity_id}.gpx")
        with open(file_path, "wb") as fb:
            fb.write(file_data)
    except Exception as e:
        print(f"Failed to download activity {activity_id}: {str(e)}")
        traceback.print_exc()


async def gather_with_concurrency(n, tasks):
    semaphore = asyncio.Semaphore(n)

    async def sem_task(task):
        async with semaphore:
            return await task

    return await asyncio.gather(*(sem_task(task) for task in tasks))


def get_downloaded_ids(folder):
    return [
        i.split(".")[0]
        for i in os.listdir(folder)
        if i.endswith(".gpx") and not i.startswith(".")
    ]


def download_new_activities(secret_path, is_cn, downloaded_ids, folder):
    api = Garmin(secret_path, is_cn)
    activity_ids = api.get_activity_id_list()
    print(f"all activity_ids size is {len(activity_ids)}")
    to_generate_garmin_ids = list(set(activity_ids) - set(downloaded_ids))
    print(f"{len(to_generate_garmin_ids)} new activities to be downloaded")

    start_time = time.time()
    for activity_id in to_generate_garmin_ids:
        download_garmin_data(api, activity_id, folder)
    print(f"Download finished. Elapsed {time.time() - start_time} seconds")
    return to_generate_garmin_ids


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--user", action="store", required=True, help="email")
    parser.add_argument("-p", "--pwd", action="store", required=True, help="pwd")
    parser.add_argument(
        "--is-cn",
        dest="is_cn",
        action="store_true",
        help="if garmin accout is cn",
    )
    parser.add_argument(
        "--out",
        dest="out_dir",
        action="store",
        default="garmin_export_out",
        help="download out file dir",
    )
    options = parser.parse_args()

    p = '.garth_' + str(int(options.is_cn)) + "_" + options.user
    login_ok = GarminLogin(options.user, options.pwd, options.is_cn).gen_secret(p)
    if not login_ok:
        print('login failed')
        exit(-1)

    folder = options.out_dir
    # make gpx or tcx dir
    if not os.path.exists(folder):
        os.mkdir(folder)
    downloaded_ids = get_downloaded_ids(folder)

    print(f'downloaded_ids size: {len(downloaded_ids)}')

    download_new_activities(
        p,
        options.is_cn,
        downloaded_ids,
        folder,
    )

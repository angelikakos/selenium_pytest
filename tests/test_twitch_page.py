from pages.twitch_page import TwitchPage
import logging

logger = logging.getLogger(__name__)


def test_twitch_page():
    twitchPage = TwitchPage()
    logger.info("The test is started.")
    twitchPage.goToMainPage()
    twitchPage.goSearch()
    twitchPage.goToStarCraft()
    twitchPage.scrollTwoTimes()
    twitchPage.open1Streamer()
    twitchPage.takeScreenShot()
    twitchPage.exit()
    logger.info('The test is Finished')

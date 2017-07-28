import datetime

from google.appengine.ext import ndb


class BieberImage(ndb.Model):
  """A posted Bieber GIF."""
  title = ndb.StringProperty()
  image_url = ndb.StringProperty()
  time_posted = ndb.DateProperty()
  votes = ndb.IntegerProperty()
  tags = ndb.StringProperty(repeated = True)


def new_image(title, url, tags):
  """Puts a new Bieber GIF to Datastore."""
  image = BieberImage(title=title, image_url=url, time_posted=datetime.datetime.now(), tags=tags)
  return image.put()

def get_top_ten():
  """Fetches the top ten ranked Bieber GIFs."""
  query = BieberImage.query().order(-BieberImage.votes)
  return query.fetch(limit=10)

def get_recent():
  """Fetches all GIFs posted in the past hour."""
  one_hour_ago = datetime.datetime.now() - datetime.timedelta(hours=1)
  query = BieberImage.query(BieberImage.time_posted >= one_hour_ago)
  return query.fetch(limit=10)

def get_by_tag(tag):
  """Fetches all GIFs with the given tag."""
  query = BieberImage.query(BieberImage.tags == "#" + tag)
  return query.fetch(limit=10)

def upvote(title):
  """Upvotes the given Bieber GIF."""
  query = BieberImage.query(BieberImage.title == title)
  result = query.get()
  if result:
    if not result.votes:
      result.votes = 1
    else:
      result.votes += 1
    result.put()
    return result
